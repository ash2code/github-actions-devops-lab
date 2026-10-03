def add(first: float, second: float) -> float:
	return first + second


def subtract(first: float, second: float) -> float:
	return first - second


def multiply(first: float, second: float) -> float:
	return first * second


def divide(first: float, second: float) -> float:
	if second == 0:
		raise ValueError("Cannot divide by zero")
	return first / second
