# HitideConfigGenerator

## Overview
This package is used to create configuration JSON files which specify input parameters for the [forge](https://github.com/podaac/forge), [forge-py](https://github.com/podaac/forge-py) and [tig](https://github.com/podaac/tig) software - these software generate geographic coverage footprints and variable thumbnails for granules, which are utilized by user-facing services such as HiTIDE and Earthdata Search. The same config file is used as input to all 3 of these tools, with one file per collection.  The config generator's intention is to simplify the process of making these config files, as well as validate the config file format against a predefined schema..

The config JSON serves as a small metadata side car file for the granules in a collection, with one config file generated per collection. This package both creates and validates the config file format against a predefined schema.

## Features
- Generate structured configuration objects for forge, forge-py, tig, and HiTIDE processing.
- Supports optional parameters for customization.
- Validates configuration against a predefined JSON schema.
- Saves the configuration to a JSON file.

## Installation
```sh
pip install forge-tig-config-generator
```

## Usage

### Creating a Configuration Generator Instance
```python
from podaac.forge_tig_config_generator.generate_config import HitideConfigGenerator
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
The arg names / values passed to `HitideConfigGenerator` become the keys / values in the dictionary and JSON. Because the main purpose of the JSON is to be used with forge-py and tig, the args relevant to each are split below. Detailed descriptions of these args are on the respective read-me pages (where the args are alternately refered to as "config parameters" or "fields"). Config files can be generated for use with either forge-py or tig separately, or both. It is only necessary to pass the args relevant to the software intended for use with the config file. 

### args relevant to forge-py footprinter

`shortName` (str, required), `latVar` (str, required), `lonVar` (str, required), `is360` (bool, required), `timeVar` (str, optional), `strategy` (str, optional), `open_cv` (dict, optional), `alpha_shape` (dict, optional), `shapely_linstring` (dict, optional).

Detailed descriptions of the args can be found on the [forge-py readme](https://github.com/podaac/forge-py?tab=readme-ov-file#description-of-fields).

### args relevant to tig image generation

`shortName` (str, required), `latVar` (str, required), `lonVar` (str, required), `is360` (bool, required), `imgVariables` (list of dicts, required), `image` (dict, optional).

Detailed descriptions of the args can be found on the [tig readme](https://github.com/podaac/tig?tab=readme-ov-file#description-of-fields).

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
