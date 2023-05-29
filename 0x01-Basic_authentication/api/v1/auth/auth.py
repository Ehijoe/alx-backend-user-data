#!/usr/bin/env python3
"""Authentication system."""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Apply authentication to certain paths."""
        return False

    def authorization_header(self, request=None) -> str:
        """To be implemented."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user."""
        return None
