def calculate(first_number: float, operator: str, second_number: float) -> float:
	if operator == "+":
		return first_number + second_number
	if operator == "/":
		if second_number == 0:
			raise ZeroDivisionError("Cannot divide by zero.")
		return first_number / second_number
	raise ValueError(f"Unsupported operator: {operator}")


def main() -> None:
	try:
		first_number = float(input("First number: "))
		operator = input("Operator (+, /): ").strip()
		second_number = float(input("Second number: "))
		result = calculate(first_number, operator, second_number)
	except ValueError as error:
		print(f"Error: {error}")
		return
	except ZeroDivisionError as error:
		print(f"Error: {error}")
		return

	print(f"Result: {result}")


if __name__ == "__main__":
	main()
