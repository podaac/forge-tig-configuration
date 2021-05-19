# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 
### Added
- **PODAAC-3276**
  - Generated collection_name.cfg file through persistent-id.cfg
  - program ran against dataset-config-overrides project's production folder against L2SS TEST DB.  There are 14 files not able to find cross reference, Hence, not able to translate to their relative collection_name.cfg.  rename_cfg python code output as follow:
  - refer to the unprocessed-files for the list of files which are not processed (probably need to be done manually)

   .....
    INFO:__main__:/Users/eyen/development/L2SS-ingest/dataset-config-overrides/production/PODAAC-CYGNS-C2H10.cfg ---     Copying to ---> /tmp/cfgs/CYGNSS_L2_SURFACE_FLUX_CDR_V1.0.cfg
    INFO:__main__:/Users/eyen/development/L2SS-ingest/dataset-config-overrides/production/PODAAC-CYGNS-L2X30.cfg does not exist as a file
    INFO:__main__:/Users/eyen/development/L2SS-ingest/dataset-config-overrides/production/PODAAC-QSX12-L2B41.cfg --- Copying to ---> /tmp/cfgs/QSCAT_LEVEL_2B_OWV_COMP_12_KUSST_LCRES_4.1.cfg
    INFO:__main__:/Users/eyen/development/L2SS-ingest/dataset-config-overrides/production/PODAAC-GHMDA-2PJ19.cfg --- Copying to ---> /tmp/cfgs/MODIS_A-JPL-L2P-v2019.0.cfg
    INFO:__main__:There are 14 of files unprocessed:
    ERROR:__main__:Unprocessed: PODAAC-GHMDT-2PJ01.cfg
    ERROR:__main__:Unprocessed: PODAAC-GHG16-2PO27.cfg
    ERROR:__main__:Unprocessed: PODAAC-GHAMS-2PR01.cfg
    ERROR:__main__:Unprocessed: PODAAC-SMP30-2SOCS.cfg
    ERROR:__main__:Unprocessed: PODAAC-SMP3A-2SOCS.cfg
    ERROR:__main__:Unprocessed: PODAAC-GHVRS-2PN16.cfg
    ERROR:__main__:Unprocessed: PODAAC-GHMDA-2PJ01.cfg
    ERROR:__main__:Unprocessed: AVHRR_SST_METOP_B-OSISAF-L2P-v1.0.cfg
    ERROR:__main__:Unprocessed: PODAAC-OSCAR-03D01.cfg
    ERROR:__main__:Unprocessed: PODAAC-GHGMR-4FJ04.cfg
    ERROR:__main__:Unprocessed: PODAAC-J1SHA-NETGC.cfg
    ERROR:__main__:Unprocessed: PODAAC-J1SHA-NETCC.cfg
    ERROR:__main__:Unprocessed: PODAAC-AQR40-3S1CS.cfg
    ERROR:__main__:Unprocessed: PODAAC-GHATS-2PU01.cfg
    INFO:__main__:Successfully ran the program and close DB connection

### Changed
### Deprecated
### Removed
### Fixed
### Security