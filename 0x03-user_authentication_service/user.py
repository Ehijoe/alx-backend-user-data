#!/usr/bin/env python3
"""Class for Users."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """Database Model for Users."""

    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    hashed_password = Column("hashed_password", String, nullable=False)
    session_id = Column("session_id", String, nullable=True)
    reset_token = Column("reset_token", String, nullable=True)
