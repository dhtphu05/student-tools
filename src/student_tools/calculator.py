"""Basic calculator operations."""

from .validator import validate_number

class DivisionByZeroError(ValueError, ZeroDivisionError):
    """Raised when division by zero is attempted in calculator operations."""
    pass


def add(first: object, second: object) -> float:
    """Return the sum of two numbers."""
    return validate_number(first, "first") + validate_number(second, "second")


def subtract(first: object, second: object) -> float:
    """Return the difference between two numbers."""
    return validate_number(first, "first") - validate_number(second, "second")


def multiply(first: object, second: object) -> float:
    """Return the product of two numbers."""
    return validate_number(first, "first") * validate_number(second, "second")


def divide(first: object, second: object) -> float:
    """Return the quotient of two numbers.

    Raises:
        DivisionByZeroError: If ``second`` is zero.
        ValueError: If ``first`` or ``second`` is not a valid number,
            or as ``DivisionByZeroError`` inherits from ``ValueError``.
    """
    first_number = validate_number(first, "first")
    second_number = validate_number(second, "second")
    if second_number == 0:
        raise DivisionByZeroError("cannot divide by zero")
    return first_number / second_number
