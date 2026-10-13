import unittest

from app import calculate


class CalculateTests(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(calculate(8, "+", 3), 11)

	def test_division(self):
		self.assertEqual(calculate(8, "/", 2), 4)

	def test_division_by_zero_raises_error(self):
		with self.assertRaises(ZeroDivisionError):
			calculate(8, "/", 0)

	def test_unsupported_operator_raises_error(self):
		with self.assertRaises(ValueError):
			calculate(8, "%", 3)


if __name__ == "__main__":
	unittest.main()
