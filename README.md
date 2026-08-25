# Spline–PBG–PTFE THz Antenna

This research repository contains the shareable data, figure assets, metadata, scripts, manuscript sources, and journal-specific submission versions for the THz spline-optimized antenna study.

## Source-of-truth policy

The scientific baseline is stored in `manuscripts/master/`. Scientific values, methods, citations, and conclusions must be corrected there first. Journal-specific derivatives are stored under `manuscripts/journals/` and may adapt the document class, metadata, declarations, table placement, figure paths, and citation style without silently changing the scientific content.

The repository is organized so that Manus can inspect, audit, and prepare changes through a branch and Pull Request. No correction should be applied independently to only one journal version unless it is genuinely journal-specific.

## Repository structure

```text
manuscripts/
  master/                         Common scientific baseline
  assets/figures/                Curated names used by LaTeX sources
  journals/
    frequenz/                     De Gruyter Frequenz version
    aeu/                          Elsevier AEÜ version
    radio-science/                AGU Radio Science version
    motl/                         Wiley MOTL placeholder/version
metadata/                         Antenna, material, and PBG parameters
figure_data/                      Numerical data and original figure exports
simulation_results/               Documentation for CST/HFSS result storage
scripts/                          Reproducibility and post-processing scripts
reports/                          Journal conversion and guideline reports
audits/                           Visual, reference, and submission audits
CHANGELOG.md                      Human-readable change history
REPOSITORY_WORKFLOW.md            Detailed GitHub and Overleaf procedure
```

## Overleaf workflow

Use one Overleaf project per journal. Keep the master scientific version separate from Frequenz, AEÜ, Radio Science, and MOTL. Overleaf is used for collaborative writing, comments, Track Changes, and PDF compilation; GitHub is used for the durable history, review, and archival submission states.

Before synchronizing, finish or export active Track Changes and comments. Pull before pushing, compile after every substantial change, and archive each submitted state with a descriptive Git tag or release, such as `frequenz-submission-v1.0`.

## Scientific and data policy

Only shareable files are included. Proprietary CST/HFSS project files remain excluded where licensing or institutional restrictions apply. No passwords, API keys, or confidential institutional files belong in this repository.

The data and code licenses are intentionally separated:

- `LICENSE-CODE-MIT.txt` applies to reusable scripts.
- `LICENSE-DATA-CC-BY-4.0.txt` applies to shareable metadata, figure data, and simulation-result exports where permitted.

## Validation before submission

Before any submission, verify the author metadata, affiliations, postal address, ORCID identifiers, bibliography and DOI records, figure resolution, journal declarations, data-availability statement, AI disclosure, and the exact PDF generated from the submitted source.
