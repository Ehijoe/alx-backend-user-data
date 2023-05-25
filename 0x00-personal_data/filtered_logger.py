#!/usr/bin/env python3
"""Filtered Logger."""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Redact sensitive fields from data."""
    for field in fields:
        print(message)
        message = re.sub(f"{field}=[^{separator}]*{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
