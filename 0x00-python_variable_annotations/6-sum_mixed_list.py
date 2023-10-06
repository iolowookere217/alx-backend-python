#!/usr/bin/env python3
"""This module defines an annoated function `sum_mixed_list`"""
from typing import Union, List


def sum_mixed_list(mixd_list: List[Union[int, float]]) -> float:
    """returns the sum of list element as float"""
    return float(sum(mixd_list))
