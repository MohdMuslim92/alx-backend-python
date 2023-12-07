#!/usr/bin/env python3

"""Module that takes a list mxd_lst of integers and floats as argument and
returns their sum as a float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats and return the sum as a float."""
    return sum(mxd_lst)
