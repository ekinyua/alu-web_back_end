#!/usr/bin/env python3
""" Range simple helper fun """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Args:
            page: Current page
            page_size: Total size of the page

        Return:
            tuple with the range start and end size page
    """

    final_index: int = page * page_size
    start_index: int = final_index - page_size

    return (start_index, final_index)
