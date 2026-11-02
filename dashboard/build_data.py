#!/usr/bin/env python3
"""Build site/data.json for the JuliaSmoothOptimizers dashboard.

Sources:
  * GitHub REST API           -> org repositories, stars
  * General registry (clone)  -> UUIDs, latest versions, dependents
  * Julia package server logs -> unique downloads over the last 14 days

Usage: build_data.py REGISTRY_DIR OUT_JSON   (GITHUB_TOKEN optional but recommended)
"""
import csv
import datetime as dt
import gzip
import io
import json
import os
import re
import sys
import tomllib
import urllib.request
from collections import defaultdict
from pathlib import Path

ORG = "JuliaSmoothOptimizers"
DAYS = 14
LOGS = "https://julialang-logs.s3.amazonaws.com/public_outputs/current/package_requests_by_date.csv.gz"


def http(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    return urllib.request.urlopen(req, timeout=120)


def gh_paged(path, tolerant=False):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "jso-dashboard"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    sep = "&" if "?" in path else "?"
    items, page = [], 1
    while True:
        try:
            with http(f"https://api.github.com{path}{sep}per_page=100&page={page}", headers) as r:
                batch = json.load(r)
        except Exception as e:
            if not tolerant:
                raise
            # e.g. empty repo (204) or a contributor list too large for the API
            print(f"{path}: {e}", file=sys.stderr)
            return items
        items += batch
        if len(batch) < 100:
            return items
        page += 1


def gh_repos():
    return gh_paged(f"/orgs/{ORG}/repos?type=public")


def gh_contributors(repo):
    return [
        {"login": c["login"], "avatar": c["avatar_url"], "url": c["html_url"], "commits": c["contributions"]}
        for c in gh_paged(f"/repos/{ORG}/{repo}/contributors", tolerant=True)
        if isinstance(c, dict) and c.get("type") != "Bot"
    ]


def gh_descriptions(slugs):
    """Fetch description and stars via batched GraphQL queries; returns {(owner, repo): (text, stars)}."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set; skipping dependent descriptions and stars", file=sys.stderr)
        return {}
    slugs = sorted(slugs)
    out = {}
    for i in range(0, len(slugs), 50):
        chunk = slugs[i : i + 50]
        q = "query{" + " ".join(
            f'r{j}:repository(owner:{json.dumps(o)},name:{json.dumps(n)}){{description stargazerCount}}'
            for j, (o, n) in enumerate(chunk)
        ) + "}"
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=json.dumps({"query": q}).encode(),
            headers={"Authorization": "Bearer " + token, "User-Agent": "jso-dashboard"},
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                res = json.load(r).get("data") or {}
        except Exception as e:  # descriptions are optional
            print("GraphQL batch failed:", e, file=sys.stderr)
            continue
        for j, slug in enumerate(chunk):
            node = res.get(f"r{j}")
            if node:
                out[slug] = ((node.get("description") or "").strip(), node["stargazerCount"])
    return out


def vtuple(s):
    return tuple(int(x) for x in re.split(r"[.+-]", s)[:3])


def parse_bound(s):
    return tuple(int(x) for x in s.split("."))


def in_range(ver, spec):
    """Check (major, minor, patch) against a registry compressed range like '0.3-0.5'."""
    lo, _, hi = spec.partition("-")
    hi = hi or lo
    lo_t, hi_t = parse_bound(lo), parse_bound(hi)
    lo_t = lo_t + (0,) * (3 - len(lo_t))
    return ver >= lo_t and ver[: len(hi_t)] <= hi_t


def repo_slug(url):
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", url.strip())
    return (m.group(1), m.group(2)) if m else None


def load_registry(root):
    pkgs = {}
    for pkg_toml in Path(root).glob("*/*/Package.toml"):
        d = pkg_toml.parent
        info = tomllib.loads(pkg_toml.read_text())
        vfile = d / "Versions.toml"
        versions = tomllib.loads(vfile.read_text()) if vfile.exists() else {}
        live = [vtuple(v) for v, meta in versions.items() if not meta.get("yanked")]
        if not live:
            continue
        dfile = d / "Deps.toml"
        deps = tomllib.loads(dfile.read_text()) if dfile.exists() else {}
        latest = max(live)
        dep_uuids = set()
        for spec, table in deps.items():
            if isinstance(table, dict) and in_range(latest, spec):
                dep_uuids.update(v for v in table.values() if isinstance(v, str))
        pkgs[info["uuid"]] = {
            "name": info["name"],
            "repo": info.get("repo", ""),
            "subdir": info.get("subdir", ""),
            "latest": ".".join(map(str, latest)),
            "deps": dep_uuids,
        }
    return pkgs


def downloads(uuids):
    with http(LOGS) as r:
        raw = gzip.decompress(r.read()).decode()
    rows = list(csv.DictReader(io.StringIO(raw)))
    last = max(r["date"] for r in rows)
    start = (dt.date.fromisoformat(last) - dt.timedelta(days=DAYS - 1)).isoformat()
    totals = defaultdict(int)
    for r in rows:
        if r["package_uuid"] in uuids and start <= r["date"] <= last:
            # request_addrs = distinct client addresses that day, summed over the window
            totals[r["package_uuid"]] += int(r["request_addrs"])
    return totals, start, last


def main():
    registry_dir, out = sys.argv[1], sys.argv[2]
    repos = [r for r in gh_repos() if not r["fork"] and r.get("language") == "Julia"]
    registry = load_registry(registry_dir)

    by_repo = {}
    for uuid, p in registry.items():
        slug = repo_slug(p["repo"])
        if slug and slug[0].lower() == ORG.lower():
            by_repo[slug[1].lower()] = uuid
    jso_uuids = set(by_repo.values())
    dl, start, end = downloads(jso_uuids)

    dependents = defaultdict(list)
    for uuid, p in registry.items():
        for dep in p["deps"] & jso_uuids:
            if dep != uuid:
                slug = repo_slug(p["repo"])
                dependents[dep].append({
                    "name": p["name"],
                    "url": (f"https://github.com/{slug[0]}/{slug[1]}" + (f"/tree/HEAD/{p['subdir']}" if p["subdir"] else "")) if slug else None,
                    "repo_url": f"https://github.com/{slug[0]}/{slug[1]}" if slug else None,
                    "subdir": p["subdir"],
                    "jso": uuid in jso_uuids,
                    "slug": slug,
                })

    descs = gh_descriptions({d["slug"] for ds in dependents.values() for d in ds if d["slug"]})
    for ds in dependents.values():
        for d in ds:
            d["description"], d["stars"] = descs.get(d.pop("slug"), ("", 0))
        ds.sort(key=lambda d: (-d["stars"], d["name"].lower()))

    packages = []
    for r in repos:
        uuid = by_repo.get(r["name"].lower())
        deps = dependents.get(uuid, []) if uuid else []
        packages.append({
            "name": registry[uuid]["name"] if uuid else r["name"],
            "url": r["html_url"],
            "description": r.get("description") or "",
            "archived": r["archived"],
            "stars": r["stargazers_count"],
            "registered": bool(uuid),
            "version": registry[uuid]["latest"] if uuid else None,
            "downloads": dl.get(uuid, 0) if uuid else None,
            "dependents": deps,
            "contributors": gh_contributors(r["name"]),
        })

    data = {
        "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "downloads_window": {"start": start, "end": end, "days": DAYS},
        "packages": packages,
    }
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(data, indent=1))
    print(f"{len(packages)} packages, {sum(p['registered'] for p in packages)} registered")


if __name__ == "__main__":
    main()
