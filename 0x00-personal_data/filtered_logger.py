#!/usr/bin/env python3
"""
Module to obfuscate log messages.
"""

import re

patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
       """
    Obfuscate log message by replacing specified fields with redaction.

    Args:
        fields (list of str): Fields to obfuscate.
        redaction (str): String to replace obfuscated fields.
        message (str): Log line message.
        separator (str): Character separating fields in the log line.

    Returns:
        str: Obfuscated log message.
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
