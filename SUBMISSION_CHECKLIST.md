# Submission checklist

Use this checklist before creating a submission tag or uploading a manuscript to a journal.

## Scientific consistency

- [ ] All scientific corrections were first applied to `manuscripts/master/`.
- [ ] The affected journal derivative contains the same validated numerical values, methods, figures, and conclusions.
- [ ] Figure captions, labels, cross-references, units, and negative S11 values were checked.
- [ ] The comparison table is consistent with the benchmarking text and cited literature.

## LaTeX and bibliography

- [ ] `python3 scripts/audit_manuscripts.py` passes.
- [ ] The journal’s official class, template, bibliography style, and submission declarations are used.
- [ ] The source compiles in the corresponding Overleaf project.
- [ ] No `.aux`, `.log`, `.bbl`, `.blg`, `.synctex.gz`, or other generated files are committed.
- [ ] The PDF has been inspected page by page for overflow, missing figures, unreadable tables, and reference-list errors.

## Editorial metadata

- [ ] Author names, affiliations, corresponding-author email, postal address, and ORCID values are correct.
- [ ] Abstract length and keyword count satisfy the target journal.
- [ ] Funding, conflict-of-interest, ethics, consent, data availability, and AI disclosure statements match the journal requirements.
- [ ] Cover letter and highlights, when required, are stored with the journal version.

## Archiving

- [ ] Track Changes and comments have been finalized before synchronization.
- [ ] The exact source ZIP and compiled PDF have been saved outside the live Overleaf editing state.
- [ ] The accepted submission state has a descriptive Git tag, for example `frequenz-submission-v1.0`.
- [ ] The tag points to the exact commit sent to the journal.
- [ ] Any repository-publication or Zenodo release decision has been reviewed separately from the manuscript submission.
