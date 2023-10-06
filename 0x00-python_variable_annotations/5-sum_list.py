#!/usr/bin/env python3
"""This module defines an annotated function `sum_list`"""
from typing import List


def sum_list(my_list: List[float]) -> float:
    """returns the sum of list elements as float"""
    return float(sum(my_list))
