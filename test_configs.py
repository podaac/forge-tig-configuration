import os
import json
import pytest

# Directory containing the configuration files
CONFIG_DIR = 'config-files'

@pytest.mark.parametrize("config_file", [
    os.path.join(CONFIG_DIR, f) for f in os.listdir(CONFIG_DIR) if f.endswith('.cfg')
])
def test_json_loadable(config_file):
    """Test if a configuration file can be loaded as JSON."""
    with open(config_file, 'r') as f:
        try:
            json.load(f)
        except json.JSONDecodeError as e:
            pytest.fail(f"Failed to load JSON from {config_file}: {e}")
