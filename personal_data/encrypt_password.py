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
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
