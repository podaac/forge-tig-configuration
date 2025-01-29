"""script used to generate forge tig configuration"""

import ast
import json
import os
from typing import Dict, Any, Optional
import click
import numpy as np
import pandas as pd
from jsonschema import validate


class HiTideConfigGenerator:
    """Class to generate configurations"""

    REQUIRED_SETTINGS_SHEET = "required-settings"
    FORGE_PY_SHEET = "forge-py"
    TIG_SHEET = "tig"

    @staticmethod
    def _convert_value(value: Any) -> Any:
        """Convert non-standard types to JSON-serializable types."""
        if pd.isna(value):
            return None
        if isinstance(value, (pd.Timestamp, np.datetime64)):
            return str(value)
        if isinstance(value, (np.bool_, bool)):
            return bool(value)
        if isinstance(value, (np.integer, int)):
            return int(value)
        if isinstance(value, (np.floating, float)):
            return float(value)
        return value

    @classmethod
    def filter_config_to_schema(cls, config: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
        """Filter configuration to match only schema-defined fields."""
        def recursive_filter(current_config, current_schema):
            if current_schema.get('type') == 'object':
                filtered_obj = {}
                for key, value in current_config.items():
                    prop_schema = current_schema.get('properties', {}).get(key, {})
                    if prop_schema:
                        if prop_schema.get('type') == 'object' and isinstance(value, dict):
                            filtered_value = recursive_filter(value, prop_schema)
                            if filtered_value:
                                filtered_obj[key] = filtered_value
                        elif prop_schema.get('type') == 'array' and isinstance(value, list):
                            filtered_obj[key] = [
                                recursive_filter(item, prop_schema.get('items', {}))
                                for item in value if item
                            ]
                        else:
                            filtered_obj[key] = value
                return filtered_obj
            return current_config

        return recursive_filter(config, schema)

    @classmethod
    def generate_configuration(cls, file_path: str) -> Optional[Dict[str, Any]]:
        """Generate configuration from Excel file."""
        # Load required data
        required_settings = cls.read_sheet_as_dict(file_path, cls.REQUIRED_SETTINGS_SHEET)
        forge_py = cls.read_sheet_as_dict(file_path, cls.FORGE_PY_SHEET)
        tig_data = cls.read_sheet_as_list(file_path, cls.TIG_SHEET)

        if not all([required_settings, forge_py, tig_data]):
            return None

        # Construct strategy configuration
        strategy = forge_py.pop("strategy", None)
        thinning_method = forge_py.pop("thinning_method", None)
        thinning_value = forge_py.pop("thinning_value", None)

        if thinning_method and thinning_value:
            try:
                thinning_value = ast.literal_eval(thinning_value)
            except (ValueError, SyntaxError):
                pass  # Leave thinning_value as is if parsing fails
            forge_py["thinning"] = {"method": thinning_method, "value": thinning_value}

        strategy_dict = {"footprint": {"strategy": strategy, strategy: forge_py}}

        # Default settings
        defaults = {
            'tiles': {'steps': [30, 14]},
            'image': {'ppd': 4, 'res': 8},
            'footprinter': 'forge-py'
        }

        # Merge configurations
        config = {**required_settings, **strategy_dict, **tig_data, **defaults}

        # Load and apply schema filtering
        schema = cls.load_schema()
        return cls.filter_config_to_schema(config, schema)

    @classmethod
    def read_sheet_as_dict(cls, file_path: str, sheet_name: str) -> Optional[Dict[str, Any]]:
        """Read Excel sheet and convert to dictionary with type-safe conversion."""
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
            if df.empty:
                raise ValueError(f"Sheet '{sheet_name}' is empty")

            first_row = df.iloc[0]
            return {k: cls._convert_value(v) for k, v in first_row.items() if pd.notna(v)}
        except Exception as e:
            click.echo(f"Error reading {sheet_name}: {e}", err=True)
            return None

    @classmethod
    def read_sheet_as_list(cls, file_path: str, sheet_name: str) -> Optional[Dict[str, Any]]:
        """Read sheet as list of non-empty dictionaries."""
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
            df.dropna(how='all', inplace=True)
            return {'imgVariables': [
                {k: cls._convert_value(v) for k, v in row.items() if pd.notna(v) and v != ""}
                for row in df.to_dict(orient="records")
            ]}
        except Exception as e:
            click.echo(f"Error reading {sheet_name}: {e}", err=True)
            return None

    @staticmethod
    def load_schema() -> Dict[str, Any]:
        """Load JSON schema for validation."""
        schema_path = os.path.join(os.path.dirname(__file__), "schema.json")
        with open(schema_path, "r") as file:
            return json.load(file)


@click.command()
@click.option('-f', '--file', help='Excel file with configuration settings', required=True)
def generate_hitide_config(file: str):
    """Generate and validate HiTide configuration."""
    generator = HiTideConfigGenerator()
    config = generator.generate_configuration(file)

    if not config:
        click.echo("Configuration generation failed.", err=True)
        return

    try:
        schema = generator.load_schema()
        validate(instance=config, schema=schema)
        click.echo(json.dumps(config, indent=2))
        short_name = config.get('shortName')
        file_name = f"{short_name}.cfg"
        with open(file_name, 'w') as open_file:
            json.dump(config, open_file, indent=4)

    except Exception as e:
        click.echo(f"Validation error: {e}", err=True)


if __name__ == '__main__':
    generate_hitide_config()
