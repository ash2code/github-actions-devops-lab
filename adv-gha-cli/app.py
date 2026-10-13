def add(first_number: float, second_number: float) -> float:
    return first_number + second_number


def main() -> None:
    first_number = float(input("First number: "))
    second_number = float(input("Second number: "))
    print(f"Sum: {add(first_number, second_number)}")


if __name__ == "__main__":
    main()
