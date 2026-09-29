from datetime import datetime


def validate_text(text):
    return bool(text and text.strip())


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def validate_priority(priority):
    if not priority:
        return False

    return priority.lower() in ["high", "medium", "low"]


def validate_duration(duration):
    try:
        duration = int(duration)
        return duration > 0
    except (ValueError, TypeError):
        return False


def validate_id(value):
    try:
        value = int(value)
        return value > 0
    except (ValueError, TypeError):
        return False