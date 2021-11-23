This is the official repository that presents the dataset from the following paper:

> Nadine von Frankenberg, Patrick Ruoff, Bernd Bruegge, and Vivian Loftness. 2020. LATEST: a learning-based automated thermal environment control system. In <i>Adjunct Proceedings of the 2020 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2020 ACM International Symposium on Wearable Computers</i> (<i>UbiComp-ISWC '20</i>). Association for Computing Machinery, New York, NY, USA, 573–579. DOI:https://doi.org/10.1145/3410530.3414591


# LATEST: Occupant-Thermal-Comfort-Data-Set

This module provides the data set collected in a case study for validating the LATEST 
system described in [LATEST](https://github.com/pruoff/LATEST).

### File Descriptions
* `raw_data_from_influxdb_to_csv.ipynb` was applied to create the main data sets. It 
imports `setup.py`, which uses the files in `series/`.
The only cleaning that takes place is time step fitting and 
interchanging manual fixes due technical circumstances, such as sensor exchanges. Also, 
long periods in which no participant was at their workstation were removed.

* `data_collection_phase.csv` and `temperature_control_phase.csv` contain the main data 
sets. The former is used for training models which were deployed for collecting the 
latter.
 
* `latest.names` contains a description of the data sets and their features.

* `preprocessed_data/U#_preprocessed_data.csv` contains the fully preprocessed data 
per occupant, which was used for training the models for the temperature control phase. 

* `conda_env.yml` shows the conda environment used for the project. 

