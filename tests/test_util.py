"""Utility module tests"""
from src.mediamon import util


yaml_file = 'tests/resources/test.yml'


def test_load_yaml():
    """Test loading of YAML files."""
    expected = {'foo': {'bar': True, 'baz': 1}}
    result = util.load_yaml(yaml_file)

    assert isinstance(result, dict)
    assert result == expected
