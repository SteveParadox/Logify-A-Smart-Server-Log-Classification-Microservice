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
        # User Actions
        r"User User\d+ logged (in|out)\.": "User Action",
        r"User .* changed password successfully\.": "User Action",
        r"User .* attempted unauthorized access\.": "User Action",
        r"User .* updated profile information\.": "User Action",
        r"Account with ID .*": "User Action",
        r"User .* deleted account .*": "User Action",
        r"User .* reset MFA settings\.": "User Action",

        # System Notifications
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully\.": "System Notification",
        r"System Updated to version .*": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Disk cleanup completed successfully\.": "System Notification",
        r"File .* uploaded successfully.*": "System Notification",
        r"New device registered: .*": "System Notification",
        r"Maintenance scheduled for .*": "System Notification",
        r"Server .* is back online\.": "System Notification",
        r"Security patch applied successfully\.": "System Notification",
        r"Resource usage exceeded threshold.*": "System Notification",
    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label

    return "Unclassified"
