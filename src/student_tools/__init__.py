"""Small, dependency-free utilities for students."""

from .calculator import DivisionByZeroError, add, divide, multiply, subtract
from .converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
)
from .validator import is_non_empty, is_number

__all__ = [
    "DivisionByZeroError",
    "add",
    "divide",
    "multiply",
    "subtract",
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "kilometers_to_miles",
    "miles_to_kilometers",
    "is_non_empty",
    "is_number",
]

