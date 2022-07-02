"""Utility methods"""

__all__ = [
    'load_yaml',
]

import os
import yaml


def load_yaml(path: os.PathLike) -> dict:
    """Load a YAML file and return dictionary."""
    with open(path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
