#!/usr/bin/env python3
"""Session Authentication."""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Auth class."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a new session for a user."""
        if type(user_id) is not str:
            return None
        sesh_id = str(uuid.uuid4())
        self.user_id_by_session_id[sesh_id] = user_id
        return sesh_id
