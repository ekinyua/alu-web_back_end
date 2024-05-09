#!/usr/bin/env python3
"""
    Callable function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: factor (float)

        Return:
            function that multiplies a float by multiplier
    """

    def x(f: float) -> float:
        """ Get the second argument somthing like JS """
        return float(f * multiplier)

    return x
