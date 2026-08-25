# Journal versions and Overleaf projects

Each subdirectory is a separate journal derivative. Create one Overleaf project per journal and keep its source aligned with the corresponding directory. The master scientific source remains in `../master/` and should not be replaced by a journal-specific class or declaration.

| Journal | Source directory | Current status |
|---|---|---|
| Frequenz | `frequenz/` | Source and bibliography present; final PDF was previously audited |
| AEÜ | `aeu/` | Source and bibliography present; graphical abstract asset is shared under `../assets/figures/` |
| Radio Science | `radio-science/` | Source and bibliography present |
| MOTL | `motl/` | Awaiting the authoritative final Wiley source |

A common scientific correction is first made in `../master/`, audited, and then copied or cherry-picked into the affected journal version. A journal-only correction is made only in its own directory. Every Overleaf project must be pulled or pushed deliberately; do not edit the same source file concurrently in GitHub and Overleaf.

Before submission, run the repository audit, compile in the target Overleaf project, inspect the PDF, and create a journal-specific tag such as `frequenz-submission-v1.0`.
