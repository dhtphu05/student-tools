"""Small validation helpers for user input."""


def is_number(value: object) -> bool:
    """Return whether ``value`` can be interpreted as a finite number."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return False
    return number == number and number not in (float("inf"), float("-inf"))


def validate_number(value: object, field_name: str = "value") -> float:
    """Return a numeric value or raise a clear validation error."""
    if not is_number(value):
        raise ValueError(f"{field_name} must be a finite number")
    return float(value)


def is_non_empty(value: object) -> bool:
    """Return whether ``value`` is a non-blank string."""
    return isinstance(value, str) and bool(value.strip())
