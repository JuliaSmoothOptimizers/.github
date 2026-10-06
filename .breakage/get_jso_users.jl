import Downloads, GitHub, TOML

length(ARGS) >= 1 || error("specify at least one JSO package as argument")

jso_repos, _ = GitHub.repos("JuliaSmoothOptimizers")
jso_names = [splitext(x.name)[1] for x ∈ jso_repos]

name = splitext(ARGS[1])[1]
name ∈ jso_names || error("argument should be one of ", jso_names)

dependents = String[]

# Fetches the Project.toml file from the given URL and returns it as a Dict{String, Any}
# Throws an error if the file cannot be fetched or parsed.
function fetch_toml(url)
  try
    io = Downloads.download(url, IOBuffer())  # IOBuffer holding the response
    bytes = take!(io)                         # Vector{UInt8}
    text = String(bytes)                      # raw TOML text
    project_toml = TOML.parse(text)           # Dict{String, Any}
    return project_toml
  catch e
    if isa(e, Downloads.RequestError)
      return Dict{String,Any}()
    else
      rethrow(e)
    end
  end
end

# Returns true if `pkg` is a dependency listed in the Project.toml of the package `repo` (including `extras`)
function is_dep(repo, pkg; suffix = "/Project.toml")
  repo_html = string(repo.html_url)
  branch = repo.default_branch
  repo_toml, is_dep = fetch_toml(repo_html * "/raw/$branch" * suffix), false

  if haskey(repo_toml, "deps")
    is_dep = pkg in keys(repo_toml["deps"])
  end

  if haskey(repo_toml, "extras")
    is_dep = is_dep || (pkg in keys(repo_toml["extras"]))
  end

  if haskey(repo_toml, "weakdeps")
    is_dep = is_dep || (pkg in keys(repo_toml["weakdeps"]))
  end

  return is_dep
end

# Returns true if `pkg` is a dependency listed in the Project.toml of the package `repo` under the `test` folder.
function is_test_dep(repo, pkg)
  repo_name = splitext(repo.name)[1]
  repo_name == pkg && return false  # avoid self-dependency
  return is_dep(repo, pkg; suffix = "/test/Project.toml")
end

for (repo_name, repo) in zip(jso_names, jso_repos)
  endswith(repo.name, ".jl") || continue  # Breakage.yml clones $PKG.jl.git; 
  # skips: https://github.com/JuliaSmoothOptimizers/MultiPrecisionR2
  if is_dep(repo, name)
    push!(dependents, repo_name)
  elseif is_test_dep(repo, name)
    push!(dependents, repo_name)
  end
end

println(dependents)
