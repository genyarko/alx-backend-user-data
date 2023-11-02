#!/usr/bin/env python3
"""
Module to obfuscate log messages.
"""

import re

def filter_datum(fields, redaction, message, separator):
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
    pattern = fr'(?<=^|{re.escape(separator)})(?:(?={re.escape(separator)})|({"|".join(re.escape(field) for field in fields)}))[^{re.escape(separator)}]*'
    return re.sub(pattern, redaction, message)
