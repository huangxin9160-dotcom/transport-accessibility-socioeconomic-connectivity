# Workflow overview

The computational workflow contains five steps:

1. Build travel-time catchments using road networks, land-cover impedance and topographic correction.
2. Classify service zones into Full-Service, Dual Service and Single Service zones.
3. Build a directed weighted composite socioeconomic network from mobility flows and corporate investment flows.
4. Calculate node strength and CR5 to measure network concentration.
5. Calculate Si, Ni and CCD to classify agglomerations into four coupling regimes.

The original cost-distance modelling was implemented in ArcGIS 10.8. The downstream network and indicator calculations are implemented in Python.
