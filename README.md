# spline-pbg-ptfe-thz-antenna

## Manuscript
**Title:** Spline-Optimized PBG-Enhanced PTFE Patch Antenna for the 0.35 THz Atmospheric Window
**Authors:** [Author Name(s) - INSERT]
**Target journal:** Radio Science (AGU)

## Description
This repository contains the simulation parameters, geometry descriptions, numerical result files, and figure data supporting the manuscript "Spline-Optimized PBG-Enhanced PTFE Patch Antenna for the 0.35 THz Atmospheric Window." The study is simulation-based and uses CST Microwave Studio and ANSYS HFSS. No human-subject or experimental data are included.

## Software Versions
- CST Microwave Studio: [VERSION - INSERT, e.g., 2024/2026]
- ANSYS HFSS: [VERSION - INSERT]

## Solver Settings
- Frequency range: [INSERT, e.g., 0.30-0.40 THz]
- Mesh type / cells: [INSERT]
- Boundary conditions: [INSERT]
- Excitation: [INSERT, e.g., waveguide port]

## Repository Structure
```
README.md                          This file
LICENSE                            Overview of split licensing (code vs. data)
LICENSE-CODE-MIT.txt               MIT License (applies to scripts/)
LICENSE-DATA-CC-BY-4.0.txt         CC BY 4.0 License (applies to metadata/, simulation_results/, figure_data/)
metadata/
  antenna_dimensions.csv           Patch, substrate, ground plane, and feed dimensions
  material_parameters.csv          PTFE and copper material properties
  pbg_parameters.csv               PBG lattice geometry and sweep settings
simulation_results/
  CST/                             CST Microwave Studio result exports
  HFSS/                            ANSYS HFSS result exports
figure_data/
  s11_baseline.csv                 S11 vs. frequency, baseline (no PBG) design
  s11_pbg.csv                      S11 vs. frequency, PBG-enhanced design
  gain_efficiency.csv              Gain and radiation/total efficiency vs. frequency
  radiation_patterns.csv           E-plane and H-plane radiation pattern data
scripts/
  README.md                        Description of optimization/post-processing scripts
manuscript/
  data_availability_statement.txt  Data availability statement used in the manuscript
```

## Notes
- Only non-proprietary, shareable files are included. Proprietary CST/HFSS project
  files are excluded where institutional or software licensing restricts redistribution.
- No passwords, API keys, or confidential institutional data are included.

## Citation
If you use this repository, please cite the manuscript (citation details to be added
upon publication) and the archived Zenodo release (DOI to be added after release).
