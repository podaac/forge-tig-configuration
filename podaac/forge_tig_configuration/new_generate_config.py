import pandas as pd
from pprint import pprint
import click

# Define fixed spreadsheet names
REQUIRED_SETTINGS_SHEET = "required-settings"
FORGE_PY_SHEET = "forge-py"
TIG_SHEET = "tig"

def read_excel_sheet_as_dict(file_path, sheet_name):
    """
    Reads an Excel sheet and converts the first row into a dictionary,
    using headers as keys and the first row as values. Excludes empty values.

    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to read.

    Returns:
        dict: A dictionary with header-value pairs.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        if df.empty:
            print(f"Error: The sheet '{sheet_name}' has no data rows.")
            return None

        # Use the header as keys and the first row as values
        first_row = df.iloc[0]
        return {key: value for key, value in first_row.items() if pd.notna(value)}
    except Exception as e:
        print(f"Error reading sheet '{sheet_name}': {e}")
        return None

def file_to_dict_list(file_path, sheet_name):
    """
    Reads a sheet and converts it into a list of dictionaries, where each dictionary
    represents a row with headers as keys and row values as values. Excludes empty values.

    Args:
        file_path (str): Path to the file.
        sheet_name (str): Name of the Excel sheet to read.

    Returns:
        dict: A dictionary with the list of row dictionaries.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        df.dropna(how='all', inplace=True)  # Drop rows with all empty values
        return {'imgVariables': [
            {k: v for k, v in row.items() if pd.notna(v) and v != ""}
            for row in df.to_dict(orient="records")
        ]}
    except Exception as e:
        print(f"Error reading sheet '{sheet_name}': {e}")
        return None

def generate_configuration(file_path):
    """
    Generates a configuration dictionary from the Excel file.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        dict: The generated configuration.
    """
    # Read required sheets
    required_settings = read_excel_sheet_as_dict(file_path, REQUIRED_SETTINGS_SHEET)
    forge_py = read_excel_sheet_as_dict(file_path, FORGE_PY_SHEET)
    tig_data = file_to_dict_list(file_path, TIG_SHEET)

    if not required_settings or not forge_py:
        print("Error: Missing required settings or forge-py data.")
        return None

    # Build strategy dictionary
    strategy = forge_py.get("strategy")
    filtered_args = {k: v for k, v in forge_py.items() if k != "strategy"}
    strategy_dict = {"footprint": {"strategy": strategy, strategy: filtered_args}}

    # Merge everything
    merged_config = required_settings | strategy_dict | tig_data
    return merged_config


@click.command()
@click.option('-g', '--granule', help='Sample granule file', required=True)
def generate_hitide_config_command(granule):
    """Command call to generate config"""

    generate_hitide_config(granule, dataset_id, include_image_variables, longitude, latitude, time, footprint_strategy)

if __name__ == '__main__':
    #generate_hitide_config_command()  # pylint: disable=no-value-for-parameter


    # Example usage
    file_path = "/Users/simonl/Desktop/work/podaac/forge-tig-configuration/podaac/forge_tig_configuration/example_config.xlsx"
    config = generate_configuration(file_path)


    if config:
        pprint(config)
