#!/usr/bin/env python3
"""Basic authentication."""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication class."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract base64 string from Authorization header."""
        if type(authorization_header) is not str:
            return None
        elif authorization_header[:6] == "Basic ":
            return authorization_header[6:]
        else:
            return None
