import os
import json
import pytest
from functools import lru_cache
from jsonschema import validate, ValidationError
from podaac.forge_tig_configuration import new_generate_config

@lru_cache(maxsize=1)
def get_schema():
    """Cache schema loading for performance."""
    return new_generate_config.HiTideConfigGenerator.load_schema()

def validate_config(config_file):
    """Validate single configuration file."""
    with open(config_file, "r") as f:
        config = json.load(f)
    validate(instance=config, schema=get_schema())

@pytest.mark.parametrize("config_file", [
    os.path.join('config-files', f) for f in os.listdir('config-files') if f.endswith('.cfg')
])
def test_json_schema(config_file):
    """Validate JSON configurations against schema."""
    try:
        validate_config(config_file)
    except (json.JSONDecodeError, ValidationError) as e:
        pytest.fail(f"Validation failed for {config_file}: {e}")