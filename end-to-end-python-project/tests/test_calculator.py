import pytest

from calculator import add, divide, multiply, subtract


@pytest.mark.parametrize(
	("operation", "first", "second", "expected"),
	[
		(add, 2, 3, 5),
		(subtract, 7, 4, 3),
		(multiply, 3, 4, 12),
		(divide, 8, 2, 4),
		(add, -2, 5, 3),
	],
)
def test_arithmetic_operations(operation, first, second, expected):
	assert operation(first, second) == expected


def test_divide_by_zero_raises_value_error():
	with pytest.raises(ValueError, match="Cannot divide by zero"):
		divide(10, 0)
