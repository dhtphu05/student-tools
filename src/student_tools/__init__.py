"""Small, dependency-free utilities for students."""

from .calculator import DivisionByZeroError, add, divide, multiply, subtract
from .converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kilometers_to_miles,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    miles_to_kilometers,
)
from .validator import is_non_empty, is_number, validate_number

__all__ = [
    "DivisionByZeroError",
    "add",
    "divide",
    "multiply",
    "subtract",
    "celsius_to_fahrenheit",
    "celsius_to_kelvin",
    "fahrenheit_to_celsius",
    "fahrenheit_to_kelvin",
    "kelvin_to_celsius",
    "kelvin_to_fahrenheit",
    "kilometers_to_miles",
    "miles_to_kilometers",
    "is_non_empty",
    "is_number",
    "validate_number",
]
