"""Generating hitide forge tig configuration class"""

import os
import json
from typing import Dict, Any
from jsonschema import validate


class HitideConfigGenerator:
    """
    A class to generate configuration objects adhering to a specified schema.
    """

    def __init__(
        self,
        short_name: str,
        lat_var: str,
        lon_var: str,
        is360: bool,
        time_var: str = None,
        tiles: dict = None,
        global_grid: bool = None,
        footprinter: str = "forge-py",
        tolerance: float = None,
        strategy: str = None,
        opencv_params: dict = None,
        alpha_shape_params: dict = None,
        img_variables: list = None,
        image: dict = None
    ):
        self.short_name = short_name
        self.lat_var = lat_var
        self.lon_var = lon_var
        self.is360 = is360
        self.time_var = time_var
        self.tiles = tiles
        self.global_grid = global_grid
        self.footprinter = footprinter
        self.tolerance = tolerance
        self.strategy = strategy
        self.opencv_params = opencv_params
        self.alpha_shape_params = alpha_shape_params
        self.img_variables = img_variables
        self.image = image

    def generate(self) -> dict:
        """
        Generate a configuration object adhering to the specified schema.

        Returns:
            dict: A configuration object adhering to the schema.
        """
        # Base configuration with required fields
        config = {
            "shortName": self.short_name,
            "latVar": self.lat_var,
            "lonVar": self.lon_var,
            "is360": self.is360,
        }

        # Add optional fields if provided
        if self.time_var:
            config["timeVar"] = self.time_var

        if self.tiles:
            config["tiles"] = self.tiles

        if self.global_grid is not None:
            config["global_grid"] = self.global_grid

        if self.footprinter:
            config["footprinter"] = self.footprinter

        if self.tolerance is not None:
            config["tolerance"] = self.tolerance

        # Dynamically construct footprint strategies
        footprint = {'strategy': self.strategy}
        if self.opencv_params:
            footprint['open_cv'] = self.opencv_params

        if self.alpha_shape_params:
            footprint['alpha_shape'] = self.alpha_shape_params
        config["footprint"] = footprint

        if self.img_variables:
            config["imgVariables"] = self.img_variables

        if self.image:
            config["image"] = self.image
        else:
            config["image"] = {"ppd": 4, "res": 8}

        try:
            schema = self.load_schema()
            validate(instance=config, schema=schema)
        except Exception as e:
            raise Exception(f"Validation error: {e}")

        # Specify the file path where you want to save the JSON data
        file_path = f"{self.short_name}.cfg"

        # Open the file in write mode and write the JSON data to it
        with open(file_path, "w") as json_file:
            json.dump(config, json_file, indent=4)

        return config

    @staticmethod
    def load_schema() -> Dict[str, Any]:
        """Load JSON schema for validation."""
        schema_path = os.path.join(os.path.dirname(__file__), "schema.json")
        with open(schema_path, "r") as file:
            return json.load(file)
