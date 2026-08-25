# Multi-journal workflow

## Source of truth

The scientific baseline is `manuscripts/master/master_manuscript.tex` with `manuscripts/master/references.bib`. Scientific corrections are made there first.

## Journal derivatives

Each journal directory contains a derivative source and bibliography. A journal derivative may change the document class, metadata, declarations, table placement, figure paths, and citation style, but it must not silently change scientific values.

## Recommended update sequence

1. Pull the latest repository state before editing.
2. Create a descriptive branch such as `fix/correct-s11-value`.
3. Apply and compile the master correction.
4. Record the change in `CHANGELOG.md`.
5. Propagate the validated change to the affected journal directories.
6. Compile each affected journal version.
7. Open a Pull Request for review.
8. After approval, tag the exact submission state, for example `frequenz-submission-v1.0`.

## Overleaf rule

Use one Overleaf project per journal. Do not treat Overleaf as a branch manager. Before a GitHub/Overleaf pull or push, finish or export active Track Changes and comments, because synchronization can displace them. Do not add generated `.aux`, `.log`, or other build files to the repository.
