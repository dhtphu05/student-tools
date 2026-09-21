import unittest

from student_tools.calculator import (
    DivisionByZeroError,
    add,
    divide,
    multiply,
    subtract,
)


class CalculatorTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero_raises_meaningful_error(self):
        with self.assertRaisesRegex(ValueError, "cannot divide by zero"):
            divide(10, 0)

    def test_divide_by_zero_raises_division_by_zero_error(self):
        with self.assertRaises(DivisionByZeroError):
            divide(10, 0)

    def test_division_by_zero_error_inheritance(self):
        try:
            divide(10, 0)
        except DivisionByZeroError as exc:
            self.assertIsInstance(exc, ValueError)
            self.assertIsInstance(exc, ZeroDivisionError)

    def test_divide_by_float_zero(self):
        with self.assertRaisesRegex(DivisionByZeroError, "cannot divide by zero"):
            divide(5.5, 0.0)

    def test_divide_by_negative_zero(self):
        with self.assertRaisesRegex(DivisionByZeroError, "cannot divide by zero"):
            divide(10, -0.0)

    def test_divide_zero_by_zero(self):
        with self.assertRaisesRegex(DivisionByZeroError, "cannot divide by zero"):
            divide(0, 0)

    def test_operations_validate_numeric_input(self):
        self.assertEqual(add("2", 3), 5)
        with self.assertRaisesRegex(ValueError, "first must be a finite number"):
            add("not a number", 3)


if __name__ == "__main__":
    unittest.main()
