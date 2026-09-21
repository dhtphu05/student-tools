"""Common unit conversion helpers."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9 / 5 + 32


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles."""
    return kilometers * 0.621371


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles / 0.621371

