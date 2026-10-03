import argparse


def celsius_to_fahrenheit(value):
    return value * 9 / 5 + 32


def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9


def main():
    parser = argparse.ArgumentParser(description="Convert between Celsius and Fahrenheit.")
    parser.add_argument("conversion", choices=("c-to-f", "f-to-c"))
    parser.add_argument("value", type=float)
    args = parser.parse_args()

    if args.conversion == "c-to-f":
        result = celsius_to_fahrenheit(args.value)
        unit = "F"
    else:
        result = fahrenheit_to_celsius(args.value)
        unit = "C"

    print(f"{result:.2f} {unit}")


if __name__ == "__main__":
    main()