#!/usr/bin/env python3
"""Filtered Logger."""
from typing import List
import re
import logging
from logging import StreamHandler

PII_FIELDS = ("name", "phone", "ssn", "password", "ip")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """Create a logger."""
    logger = logging.getLogger(name="user_data")
    logger.setLevel(logging.INFO)
    logger.addHandler(StreamHandler())
    logger.setFormatter(RedactingFormatter(PII_FIELDS))
    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Redact sensitive fields from data."""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
