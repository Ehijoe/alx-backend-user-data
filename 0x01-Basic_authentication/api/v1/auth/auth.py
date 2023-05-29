#!/usr/bin/env python3
"""Authentication system."""
from typing import List, TypeVar


class Auth:
    """Authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if a path requires authentication."""
        if path is None or excluded_paths is None or len(path) == 0:
            return True
        new_path = path if path[-1] == "/" else path + "/"
        return new_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """To be implemented."""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user."""
        return None
