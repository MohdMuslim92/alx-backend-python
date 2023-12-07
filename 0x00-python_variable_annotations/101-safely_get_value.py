#!/usr/bin/env python3

"""Module for safely retrieving values from a dictionary."""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary if it exists, otherwise
    returns the default value.

    Args:
        dct: A mapping/dictionary.
        key: The key to search for in the dictionary.
        default: The default value to return if the key is not found
        (default is None).

    Returns:
    The value corresponding to the key in the dictionary if present,
    else returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
