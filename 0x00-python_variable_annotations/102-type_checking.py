#!/usr/bin/env python3

"""Module for zooming elements in a tuple."""
from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in elements in a tuple by repeating them according to the
    specified factor.

    Args:
        lst: The tuple containing elements to be zoomed.
        factor: The factor by which each element in the tuple is repeated
        (default is 2).

    Returns:
        A list containing the zoomed elements from the input tuple.
    """
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(factor)
        )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
