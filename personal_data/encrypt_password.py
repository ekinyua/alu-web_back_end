#!/usr/bin/env python3
""" password encryption"""

import bcrypt


def hash_password(password):
    """
    Hashes the given password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check if password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
