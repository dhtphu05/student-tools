import unittest

from student_tools.validator import is_non_empty, is_number, validate_number


class ValidatorTests(unittest.TestCase):
    def test_number_validation(self):
        self.assertTrue(is_number("12.5"))
        self.assertTrue(is_number(-3))
        self.assertFalse(is_number("not a number"))
        self.assertFalse(is_number(None))
        self.assertFalse(is_number(float("inf")))

    def test_empty_string(self):
        self.assertFalse(is_number(""))

    def test_validate_number_returns_float(self):
        self.assertEqual(validate_number("10"), 10.0)
        self.assertEqual(validate_number(10.5), 10.5)

    def test_validate_number_raises_meaningful_error(self):
        with self.assertRaisesRegex(ValueError, "score must be a finite number"):
            validate_number("abc", field_name="score")

    def test_non_empty_validation(self):
        self.assertTrue(is_non_empty("student"))
        self.assertFalse(is_non_empty("   "))
        self.assertFalse(is_non_empty(None))


if __name__ == "__main__":
    unittest.main()
