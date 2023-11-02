#!/usr/bin/env python3
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
    pattern = fr'(?<={separator}|^)({"|".join(re.escape(field) for field in fields)})(?={separator}|$)'
    return re.sub(pattern, redaction, message)

# Example usage:
fields_to_obfuscate = ["password", "credit_card"]
log_message = "User johndoe logged in with password 12345 and paid with credit_card 1234-5678-9012-3456."
separator_char = " "

obfuscated_message = filter_datum(fields_to_obfuscate, "REDACTED", log_message, separator_char)
print(obfuscated_message)
