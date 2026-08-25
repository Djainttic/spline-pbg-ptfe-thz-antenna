# Frequenz conversion and final audit report

## Status

The manuscript has been converted to the De Gruyter **Frequenz** format using the official `article`/`dgruyter` setup available in the project. The latest source compiles successfully with pdfLaTeX and BibTeX and produces a 23-page PDF preview.

| Item | Final status |
|---|---|
| Article type | Research Article |
| Abstract | 177 words; within the requested 200-word limit |
| Keywords | 6; within the requested 3–6 range |
| Citations | Numeric citation style; 29 unique citation keys checked |
| Bibliography | 29 BibTeX records; no missing citation keys or BibTeX warnings |
| Figures | 18 referenced figures; all referenced files found |
| Compilation | pdfLaTeX ×3 plus BibTeX; successful |
| PDF | 23 pages, A4 page size |
| Production placeholders | Removed from the author source; publisher-generated bibliographic metadata is not fabricated |
| Declarations | Funding, conflict of interest, data availability, and AI disclosure included |

## Main changes from the Radio Science version

The manuscript was recast from the AGU/Radio Science presentation into the De Gruyter Frequenz article structure. The title page, article type, running title, author metadata, abstract, keywords, section hierarchy, figure labels, table labels, end matter, and reference-list style were adapted to the target journal. The bibliography was retained as a clean 29-record database and checked against all citation keys used in the source.

The benchmarking section was aligned with the cleaned comparison table. The table now reports chronological entries, uses unified gain units where the source defines them, distinguishes non-comparable architectures in the Remark column, and explicitly identifies the present work as a single-element design. Redundant prose inside the table was shortened to prevent cell collisions. The wide table is supplied as a rotating full-page table so that it remains readable rather than overlapping in portrait columns.

The manuscript states that the CST and HFSS model setup can be clarified by the corresponding author upon reasonable request. This is consistent with the author’s decision not to publish the full simulation files at this stage. The AI disclosure transparently records the use of language and LaTeX assistance while excluding simulation-data generation, scientific analysis, figures, models, and conclusions from AI use.

## Final audit findings

The final PDF has no undefined citations, no missing bibliography entries, no missing figure files, and no unresolved production placeholders in the manuscript source. Figures 15–17 and their captions remain legible. The reference list is numeric and visually consistent with the required IEEE-like ordering.

The comparison table is deliberately rotated because its eight-column content is too wide for a readable portrait layout. This is technically robust and avoids the serious overlap observed in the earlier portrait version. The table appears once in the PDF and is located near the benchmarking discussion. The author should confirm that the submission portal accepts a rotated table page; if the journal requests all tables at the end or as separate files, the same source can be submitted with that workflow.

Minor LaTeX diagnostics remain: an underfull box in the title/front-matter area and a small overfull vertical box associated with float pagination. These do not produce visible clipping in the inspected PDF. They are not citation, compilation, or content errors. The rotated table may generate internal box diagnostics during construction even though the final rendered page is visually contained.

## Points requiring author validation before submission

1. **Corresponding-author postal address:** the source currently gives the institutional affiliation and city/country, but does not invent a street address. Add the exact postal address if the Frequenz submission system or De Gruyter metadata form requires it.
2. **Author metadata:** verify spelling, order, affiliations, ORCID identifiers, and the corresponding-author email in the submission portal.
3. **AI disclosure:** keep the included statement only if it accurately reflects the authors’ use of AI-assisted editing. The authors remain responsible for validating every technical and bibliographic statement.
4. **Data availability:** confirm that “available from the corresponding author upon reasonable request” is acceptable and operational for the authors. If the journal requires a repository link, add it in the source and submission form.
5. **Table workflow:** confirm whether the portal requests tables embedded in the manuscript, at the end of the manuscript, or uploaded separately. The current embedded rotating table is suitable as a review PDF but can be separated if requested.
6. **Publisher metadata:** do not enter a DOI, volume, issue, received date, accepted date, or starting page manually. These are publisher/editorial fields and should be completed by the journal or submission portal.
7. **Research claims:** before submission, recheck the numerical values in Table 5 against the final source PDFs, particularly the 2026 comparison entry and any results reported as approximate or source-defined.

## Recommended submission contents

Submit the source ZIP, the compiled PDF for visual reference if the portal permits it, and any separate high-resolution figure files requested by the journal. Do not include auxiliary `.aux`, `.log`, `.bbl`, or temporary build files unless the portal explicitly asks for them.
