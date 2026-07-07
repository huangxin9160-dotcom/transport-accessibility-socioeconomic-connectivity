# Transport accessibility and socioeconomic connectivity in large urban systems

This repository contains custom code, sample input files, derived aggregate data templates, figure source data templates and documentation associated with the manuscript:

**Transport accessibility is insufficient for socioeconomic connectivity in large urban systems**

## Overview

The repository provides materials for reproducing the main computational workflow used to:

1. construct travel-time catchments;
2. classify service zones;
3. build composite socioeconomic networks;
4. calculate node strength and CR5;
5. calculate Spatial Integration (Si), Social Networks Connectedness (Ni), and Coupling Coordination Degree (CCD);
6. reproduce the source data underlying the main figures.

## Repository structure

- `scripts/`: analysis scripts used to calculate network and coupling indicators.
- `derived_data/`: aggregate, non-sensitive results used in the manuscript. Replace template rows with final public aggregate values before release.
- `data_sample/`: small sample input files showing required data formats.
- `figure_source_data/`: source data templates underlying Figs. 1-6. Replace template rows with final public figure source data before release.
- `docs/`: data dictionary, workflow notes and restricted-data statement.
- `config/`: parameter settings used in the analysis.

## Data restrictions

Raw mobile phone signalling data and raw corporate registration linkage records are not included because they are subject to third-party licensing, privacy and commercial restrictions. The repository provides analysis code, data schemas, sample input files, derived aggregate indices and figure source data where sharing is permitted.

## Software

The main workflow was implemented using Python 3.9, NetworkX, pandas and ArcGIS 10.8. The geospatial cost-distance workflow was originally implemented in ArcGIS 10.8. Downstream network, indicator and figure calculations can be reproduced using the provided aggregate data.

## Quick start

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run the example workflow from the repository root:

```bash
python scripts/build_composite_network.py
python scripts/calculate_cr5.py
python scripts/calculate_si_ni_ccd.py
python scripts/generate_figures.py
```

The sample inputs are intentionally small and are provided only to document file formats and calculation logic. They do not contain restricted raw data.

## Citation

Please cite the associated manuscript and the archived Zenodo release.
