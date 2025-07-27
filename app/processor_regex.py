import re

def classify_with_regex(log_message):
    """
    Classify a log message into predefined categories using regex patterns.

    Parameters:
        log_message (str): The log message to classify.

    Returns:
        str: The classification label if a pattern matches; otherwise "Unclassified".
    """
    regex_patterns = {
        r"User User\d+ logged (in|out)\.": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully\.": "System Notification",
        r"System Updated to version .*": "System Notification",
        r"File .* uploaded successfully.*": "System Notification",
        r"Disk cleanup completed successfully\.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .*": "User Action"
    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label

    return "Unclassified"
