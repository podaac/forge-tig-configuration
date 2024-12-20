# HiTide Configuration Generator

## Overview

HiTide Configuration Generator is a Python CLI tool that generates and validates configuration files for HiTide from Excel spreadsheets. It provides a flexible and type-safe way to create configuration settings for generating footprint and thumbnails.

## Features

- Generate configuration from Excel spreadsheets
- Type-safe value conversion
- JSON schema validation
- Flexible configuration generation
- CLI interface for easy use

## Prerequisites

- Python 3.10+
- Poetry
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/podaac/forge-tig-configuration.git
cd forge-tig-configuration
```

2. Install Poetry (if not already installed):
```bash
pip install poetry
```

3. Install project dependencies:
```bash
poetry install
```

## Usage

### Activating the Virtual Environment

To activate the Poetry virtual environment:
```bash
poetry shell
```

### CLI Command

```bash
generate_config -f <path_to_excel_file>
```

#### Command Options

- `-f, --file`: **[Required]** Path to the Excel file containing configuration settings
- `-h, --help`: Show help message

### Excel File Structure

Your Excel file should contain three sheets:

1. `required-settings`: Global configuration settings
2. `forge-py`: Strategy and processing configurations
3. `tig`: Image generation variables

#### Example Excel Sheets

- **required-settings**: Contains key-value pairs for global settings
- **forge-py**: Configuration for footprint strategy and processing parameters
- **tig**: List of image variables for processing

#### How to use example speadsheet

- Fill in data for each sheet, leave empty if the field doesn't apply.
- Documentation for forge-py configurations https://github.com/podaac/forge-py

## Configuration Generation Process

1. Reads specified Excel file
2. Converts data types safely
3. Merges configurations from different sheets
4. Applies JSON schema validation
5. Generates a configuration file named after the `shortName`

## Output

- Prints JSON configuration to console
- Generates a `.cfg` file named after the `shortName`

## Error Handling

- Validates input against JSON schema
- Provides detailed error messages for configuration issues
- Handles type conversions and edge cases

## Development

### Running Tests

```bash
poetry run pytest tests/
```

### Adding Dependencies

To add a new project dependency:
```bash
poetry add <package-name>
```

To add a development dependency:
```bash
poetry add --group dev <package-name>
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the Apatche License. See `LICENSE` for more information.