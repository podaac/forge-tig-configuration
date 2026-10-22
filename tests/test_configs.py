import base64
import os
import json
import urllib.error
import urllib.parse
import urllib.request
import pytest
from functools import lru_cache
from jsonschema import validate, ValidationError
from podaac.forge_tig_config_generator import generate_config

CMR_COLLECTIONS_URL = "https://cmr.earthdata.nasa.gov/search/collections.umm_json"
EDL_TOKENS_URL = "https://urs.earthdata.nasa.gov/api/users/tokens"
EDL_TOKEN_URL = "https://urs.earthdata.nasa.gov/api/users/token"

CONFIG_FILES = [f for f in os.listdir('config-files') if f.endswith('.cfg')]

@lru_cache(maxsize=1)
def get_schema():
    """Cache schema loading for performance."""
    return generate_config.HitideConfigGenerator.load_schema()

def validate_config(config_file):
    """Validate single configuration file."""
    with open(config_file, "r") as f:
        config = json.load(f)
    validate(instance=config, schema=get_schema())

@pytest.mark.parametrize("config_file", [
    os.path.join('config-files', f) for f in CONFIG_FILES
])
def test_json_schema(config_file):
    """Validate JSON configurations against schema."""
    try:
        validate_config(config_file)
    except (json.JSONDecodeError, ValidationError) as e:
        pytest.fail(f"Validation failed for {config_file}: {e}")


@lru_cache(maxsize=1)
def get_edl_token():
    """Return an Earthdata Login bearer token from CMR_USER/CMR_PASS, or None.

    Reuses an existing EDL token if the account has one, otherwise creates one.
    Returns None when credentials are unset or EDL cannot be reached, so the
    tests fall back to anonymous (public-only) CMR search.
    """
    user = os.environ.get("CMR_USER")
    password = os.environ.get("CMR_PASS")
    if not user or not password:
        return None

    auth = base64.b64encode(f"{user}:{password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}

    def _call(url, method):
        request = urllib.request.Request(url, headers=headers, method=method)
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)

    try:
        tokens = _call(EDL_TOKENS_URL, "GET")
        if isinstance(tokens, list) and tokens:
            return tokens[0].get("access_token")
        created = _call(EDL_TOKEN_URL, "POST")
        return created.get("access_token")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError):
        return None


def cmr_short_name_exists(short_name):
    """Return True if a collection with this exact (case-sensitive) short_name exists in CMR.

    Uses the public CMR collection search API. If CMR_USER/CMR_PASS are set, an
    Earthdata Login bearer token is attached so restricted (non-public)
    collections are also visible; no token is required for public collections.
    """
    query = urllib.parse.urlencode({
        "short_name": short_name,
        "options[short_name][ignore_case]": "false",
        "page_size": 1,
    })
    headers = {}
    token = get_edl_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(f"{CMR_COLLECTIONS_URL}?{query}", headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return payload.get("hits", 0) > 0


@pytest.mark.parametrize("config_file", CONFIG_FILES)
def test_short_name_matches_cmr(config_file):
    """Each config's filename and shortName must match a real CMR collection (case-sensitive)."""
    path = os.path.join('config-files', config_file)
    with open(path, "r") as f:
        config = json.load(f)

    short_name = config.get("shortName")
    expected = os.path.splitext(config_file)[0]
    assert short_name == expected, (
        f"shortName '{short_name}' does not match filename '{expected}'"
    )

    try:
        found = cmr_short_name_exists(short_name)
    except (urllib.error.URLError, TimeoutError) as e:
        pytest.skip(f"Could not reach CMR: {e}")

    assert found, (
        f"No CMR collection found for short_name '{short_name}' "
        f"(check spelling/capitalization)"
    )