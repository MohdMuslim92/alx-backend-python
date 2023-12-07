#!/usr/bin/env python3

"""Returns a function that multiplies a float by the given multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiply(x: float) -> float:
        """Multiplies a float by the given multiplier.

        Args:
            x: The float value to be multiplied.

        Returns:
            The product of the input float and the multiplier.
        """
        return x * multiplier
    return multiply
