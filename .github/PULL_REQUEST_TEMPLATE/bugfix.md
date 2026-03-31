**Indicate what bug was fixed 🐞**

A bugfix pull request should focus solely on the bugfix, and should not include any other changes such as new features or performance improvements. The pull request should clearly indicate what bug was fixed, and should reference the issue that describes the bug.

Fixes ...

**Explain how the bug was fixed**

Please link relevant documents that support your fix, such as documentation, code comments, or external resources.

**Checklist**

- [ ] The MRE from the issue is added to the test or equivalent
- [ ] The pull request does not include `Manifest.toml` or other temporary files, such as `.DS_Store`, etc.
- [ ] The code was formatted with the Julia formatter using the settings included in this repository
- [ ] All reasonable attempts were made to avoid unnecessary allocations
- [ ] The fix was done in a way that does not break public API
- [ ] All documentation related to the fix was updated
- [ ] All downstream repositories that were affected by the bug were updated
- [ ] The new code follows the [contributor guidelines](https://github.com/JuliaSmoothOptimizers/.github/blob/master/CONTRIBUTING.md).

Please also check one of the following:

- [ ] All of the new code was written by a human without the assistance of an AI
- [ ] Some of the new code was written by an AI, and the AI-generated code was reviewed and edited by a human to ensure quality and correctness
- [ ] Some of the new code was written by an AI, but the AI-generated code was NOT reviewed and edited by a human to ensure quality and correctness.

**Additional context**

Add any other context about the problem here.
