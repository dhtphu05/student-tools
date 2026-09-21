import unittest

from student_tools.converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    kilometers_to_miles,
    miles_to_kilometers,
)


class ConverterTests(unittest.TestCase):
    def test_temperature_conversion(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_negative_temperature_conversion(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)
        self.assertEqual(fahrenheit_to_celsius(-40), -40)
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67)
        self.assertAlmostEqual(fahrenheit_to_celsius(-459.67), -273.15)

    def test_temperature_round_trip(self):
        for temp_c in [0, 25, 37, -10, -40, 100]:
            temp_f = celsius_to_fahrenheit(temp_c)
            self.assertAlmostEqual(fahrenheit_to_celsius(temp_f), temp_c)

    def test_kelvin_conversion(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(celsius_to_kelvin(100), 373.15)
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0)
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(kelvin_to_celsius(373.15), 100)
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

    def test_fahrenheit_and_kelvin_conversion(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(fahrenheit_to_kelvin(212), 373.15)
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(kelvin_to_fahrenheit(373.15), 212)

    def test_distance_conversion_round_trip(self):
        miles = kilometers_to_miles(10)
        self.assertAlmostEqual(miles_to_kilometers(miles), 10)


if __name__ == "__main__":
    unittest.main()

