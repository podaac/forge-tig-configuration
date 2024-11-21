import os
import json
import pytest
from jsonschema import validate, ValidationError

# Directory containing the configuration files
CONFIG_DIR = 'config-files'

# Load the schema once
with open("schema.json", "r") as schema_file:
    SCHEMA = json.load(schema_file)

# Parameterize the test with all `.cfg` files in CONFIG_DIR
@pytest.mark.parametrize("config_file", [
    os.path.join(CONFIG_DIR, f) for f in os.listdir(CONFIG_DIR) if f.endswith('.cfg')
])
def test_json_schema(config_file):
    """Test JSON configuration files against the schema."""
    # Load the JSON config
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        pytest.fail(f"Failed to load JSON from {config_file}: {e}")

    # Validate the JSON against the schema
    try:
        validate(instance=config, schema=SCHEMA)
    except ValidationError as e:
        pytest.fail(f"Validation failed for {config_file}: {e}")