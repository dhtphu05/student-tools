"""Basic calculator operations."""


class DivisionByZeroError(ValueError, ZeroDivisionError):
    """Raised when division by zero is attempted in calculator operations."""
    pass


def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the difference between two numbers."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    return first * second


def divide(first: float, second: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        DivisionByZeroError: If ``second`` is zero.
        ValueError: As ``DivisionByZeroError`` inherits from ``ValueError``.
    """
    if second == 0:
        raise DivisionByZeroError("cannot divide by zero")
    return first / second

