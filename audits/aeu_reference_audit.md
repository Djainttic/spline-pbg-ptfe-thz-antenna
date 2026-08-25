# Final AEÜ LaTeX and BibTeX Audit

## Source audited

- LaTeX: `/home/ubuntu/upload/pasted_content_2.txt`
- BibTeX basis: `/home/ubuntu/aue_project/thz_spline_pbg_AEU_final.bib`
- Compilation: not performed in this audit.

## Citation and bibliography result

The corrected LaTeX source contains 30 distinct citation keys. The definitive AEÜ bibliography copy contains 30 records. No cited key is missing from the BibTeX file, and no BibTeX record is unused. The source uses `cas-model2-names` and `thz_spline_pbg` as its bibliography commands; rename the final file to `thz_spline_pbg.bib` or change the LaTeX command to match the filename before compiling.

## Metadata result

The full title, short title, short-author field, corresponding-author marker, email, affiliations, CRediT roles, abstract, graphical abstract, highlights, keywords, bibliography commands, author biographies, and doctoral year 2013 are present. Empty affiliation fields were removed in the uploaded source.

## Manual corrections required before submission

1. The Data Availability section still contains conditional future wording about adding a DOI. Replace it with either the actual public repository DOI or a final non-repository statement; do not submit the conditional sentence.
2. Ensure that the `.bib` filename matches `\\bibliography{thz_spline_pbg}` exactly.
3. The source contains five highlights? No: it contains three highlights, which is acceptable if each satisfies the journal's character limit. Check the final platform field separately if AEÜ requests highlights in a separate text box.
4. The bibliography includes a small number of records with author-verification notes. These notes are retained for transparency and should be removed only after the authors verify the corresponding publisher metadata.
5. The source was not compiled as part of this audit; compile in Overleaf after applying the data statement and filename decision.
