**Explain what performance issue or regression is being addressed ⚡**

A pull request for a performance improvement or regression must reference a performance issue or regression.

Fixes ...

A performance improvement pull request should focus solely on the specific performance issue, and should not include any other changes such as new features or unrelated bug fixes. The pull request should clearly indicate what performance improvement was implemented, and should reference the corresponding issue.

**Describe the performance issue or regression and how this PR addresses it**

Describe clearly and concisely what the performance issue or regression is, and how the changes in this pull request address it. Please link relevant documents that support your description, such as documentation, code comments, or external resources.

**Show some benchmarks of the performance before and after the changes**

**Checklist**

- [ ] Appropriate tests were added to ensure performance does not regress
- [ ] The pull request does not include `Manifest.toml` or other temporary files, such as `.DS_Store`, etc.
- [ ] The code was formatted with the Julia formatter using the settings included in this repository
- [ ] All reasonable attempts were made to avoid unnecessary allocations
- [ ] Package benchmarks cover the feature's performance
- [ ] The performance improvement was added in a way that does not break public API
- [ ] The new code follows the [contributor guidelines](https://github.com/SciML/.github/blob/master/CONTRIBUTING.md).

Please also check one of the following:

- [ ] All of the new code was written by a human without the assistance of an AI
- [ ] Some of the new code was written by an AI, and the AI-generated code was reviewed and edited by a human to ensure quality and correctness
- [ ] Some of the new code was written by an AI, but the AI-generated code was NOT reviewed and edited by a human to ensure quality and correctness.

**Additional context**

Add any other context about the problem here.
