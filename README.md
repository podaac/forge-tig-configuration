# HitideConfigGenerator

## Overview
`HitideConfigGenerator` is a Python class designed to generate configuration objects adhering to a specified JSON schema. It allows users to specify key parameters for HiTIDE processing and validates the generated configuration against a schema before saving it as a JSON file.

## Features
- Generate structured configuration objects for HiTIDE processing.
- Supports optional parameters for customization.
- Validates configuration against a predefined JSON schema.
- Saves the configuration to a JSON file.

## Installation
```sh
pip install podaac-forge-tig-config-generator
```

## Usage

### Creating a Configuration Generator Instance
```python
from podaac.podaac_forge_tig_config_generator.generate_config import HitideConfigGenerator
import json

config_generator = HitideConfigGenerator(
    short_name="example_dataset",
    lat_var="latitude",
    lon_var="longitude",
    is360=False,
    time_var="time",
    footprinter="forge-py",
    strategy="open_cv",
    opencv_params={
       "pixel_height": 1000,
       "simplify":0.3,
       "min_area": 30,
       "fill_value": -99999.0,
       "fill_kernel": [30,30]
    },
    alpha_shape_params={
       "alpha":0.2,
       "thinning": {"method": "bin_avg", "value": [0.5, 0.5]},
       "cutoff_lat": 80,
       "smooth_poles": [78,80],
       "simplify" : 0.3,
       "min_area": 30,
       "fill_value": -99999.0
    },
    img_variables=[
        {
            "id": "sses_bias",
            "min": "-18.85",
            "max": "19.25",
            "palette": "paletteMedspirationIndexed"
        },
        {
            "id": "sses_standard_deviation",
            "min": "-18.85",
            "max": "19.25",
            "palette": "paletteMedspirationIndexed"
        }
    ],
    image={"ppd": 8, "res": 16}
)
config = config_generator.generate()
print(json.dumps(config, indent=4))
```

### Generating and Saving the Configuration
```python
config = config_generator.generate()
print(config)  # Outputs the generated configuration
```
This method:
1. Generates a configuration dictionary.
2. Validates the configuration against a predefined schema.
3. Saves the configuration as a JSON file named `<short_name>.cfg`.

## Methods

### `generate() -> dict`
Generates a configuration object adhering to the specified schema.

- **Returns**: `dict` - The generated configuration.
- **Raises**: `Exception` if validation fails.

## Configuration Schema
The generated configuration includes:
- **Required Fields**:
  - `shortName` (str): Dataset short name.
  - `latVar` (str): Latitude variable name.
  - `lonVar` (str): Longitude variable name.
  - `is360` (bool): Whether longitude is in 0-360 format.
- **Optional Fields**:
  - `timeVar` (str): Time variable name.
  - `tiles` (dict): Grid tiling configuration.
  - `global_grid` (bool): Indicates if global grid is used.
  - `footprinter` (str): Footprint generation method.
  - `tolerance` (float): Processing tolerance.
  - `footprint` (dict): Includes footprinting strategies (OpenCV, Alpha Shape, etc.).
  - `imgVariables` (list of dict): List of image-related variables.
  - `image` (dict): Image configuration, defaults to `{"ppd": 4, "res": 8}`.

## Example Output
```json
{
    "shortName": "example_dataset",
    "latVar": "latitude",
    "lonVar": "longitude",
    "is360": false,
    "timeVar": "time",
    "footprinter": "forge-py",
    "footprint": {
        "strategy": "open_cv",
        "open_cv": {
            "pixel_height": 1000,
            "simplify": 0.3,
            "min_area": 30,
            "fill_value": -99999.0,
            "fill_kernel": [
                30,
                30
            ]
        },
        "alpha_shape": {
            "alpha": 0.2,
            "thinning": {
                "method": "bin_avg",
                "value": [
                    0.5,
                    0.5
                ]
            },
            "cutoff_lat": 80,
            "smooth_poles": [
                78,
                80
            ],
            "simplify": 0.3,
            "min_area": 30,
            "fill_value": -99999.0
        }
    },
    "imgVariables": [
        {
            "id": "sses_bias",
            "min": "-18.85",
            "max": "19.25",
            "palette": "paletteMedspirationIndexed"
        },
        {
            "id": "sses_standard_deviation",
            "min": "-18.85",
            "max": "19.25",
            "palette": "paletteMedspirationIndexed"
        }
    ],
    "image": {
        "ppd": 8,
        "res": 16
    }
}
```
