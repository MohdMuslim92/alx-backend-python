#!/usr/bin/env python3

"""Module that returns the first element of the list if it exists, otherwise
returns None."""
from typing import Any, Optional, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of the list if it exists, otherwise returns
    None."""
    if lst:
        return lst[0]
    else:
        return None
