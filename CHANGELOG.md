# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- ** PODAAC-4201 **
 - Added conf for AQUARIUS_L2_SSS_CAP_V5
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 2022-05-05

### Added
- **PODAAC-4192**
  - Added conf SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_SCIENCE_V1
- **PODAAC-4419**
  - Added conf for CYGNSS_NOAA_L2_SWSP_25KM_V1.2
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 2022-05-02

### Added
- **PODAAC-4201**
  - Added conf for AQUARIUS_L2_SSS_CAP_V5
- **PODAAC-4418**
  - Added conf for CYGNSS_L1_V2.1
  - Added conf for CYGNSS_L1_CDR_V1.1
- **PODAAC-4193**
  - Added conf SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 03-18-2022

### Added
### Changed
- **PODAAC-4182**
  - Removed `mean_square_slope` and `wind_speed_uncertainty` from CYGNSS_L2_CDR_V1.1 image variables
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 03-17-2022

### Added
- **PODAAC-4184**
  - Added conf for CYGNSS_L2_SURFACE_FLUX_CDR_V1.1
- **PODAAC-4185**
  - Added conf for CYGNSS_L2_V3.0
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 02-15-2022

### Added
- **PODAAC-4175**
  - Added conf for SMAP_JPL_L2B_NRT_SSS_CAP_V5
- **PODAAC-4182**
  - Added conf for  CYGNSS_L2_CDR_V1.1
- **PODAAC-4176**
  - Added conf for SMAP_JPL_L2B_SSS_CAP_V5
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 02-09-2022

### Added
- **PODAAC-4172**
  - Added conf for JASON_3_L2_OST_OGDR_GPS
- **PODAAC-4024**
  - Added conf for JASON-1_L2_OST_GPN_E            
  - Added conf for JASON-1_L2_OST_GPR_E            
  - Added conf for JASON-1_L2_OST_GPS_E            
  - Added conf for MERGED_TP_J1_OSTM_OST_CYCLES_V42
- **PODAAC-4189**
  - Added conf for AVHRRF_MA-STAR-L2P-v2.80
- **PODAAC-4190**
  - Added conf for AVHRRF_MB-STAR-L2P-v2.80
- **PODAAC-4191**
  - Added conf for AVHRRF_MC-STAR-L2P-v2.80
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 01-26-2022

### Added
- **PODAAC-4170**
  - Added palettes and sync to s3 bucket.
- **PODAAC-4171**
  - Added conf for AVHRRMTA_G-NAVO-L2P-v1.0
- **PODAAC-4173**
  - Added conf for AVHRRMTB_G-NAVO-L2P-v1.0
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 09-21-2020

### Added

- **PODAAC-3603**
  - Added jenkins pipeline to deploy dataset config into hitide s3 bucket.

### Changed
### Deprecated
### Removed
### Fixed
### Security

## [Released] - 05-19-2020
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
