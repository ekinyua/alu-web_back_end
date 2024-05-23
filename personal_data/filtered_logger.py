#!/usr/bin/env python3

"""Logging and handling personal data"""

import re
from typing import List
import os
import logging

def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
