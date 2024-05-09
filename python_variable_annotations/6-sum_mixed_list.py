#!/usr/bin/env python3
"""
    Mixed list annotation
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_lst: float and int numbers

        Return:
            sum of int and float numbers as a float
    """

    result: float = 0

    for x in mxd_lst:
        result += x

    return result
