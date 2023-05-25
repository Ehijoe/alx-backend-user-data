#!/usr/bin/env python3
"""Tools for handling passwords."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a user's password."""
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a password is valid."""
    return bcrypt.checkpw(password, hash_password)
