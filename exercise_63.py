""""
Ask the user for numbers repeatedly (use a list of inputs given upfront, e.g. 5 numbers).
Stop processing when a negative number is encountered.
Print the numbers processed before stopping.
This will require your use of the 'break' keyword.
"""
import sys


def main():
    try:
        number1 = int(input("Enter numbers: "))
        number2 = int(input("Enter numbers: "))
        number3 = int(input("Enter numbers: "))
        number4 = int(input("Enter numbers: "))
        number5 = int(input("Enter numbers: "))

        numbers = [number1, number2, number3, number4, number5]

        for number in numbers:
            if number < 0:
                break
            print(number)

    except ValueError:
        print("Invalid input")
    return 0


if __name__ == '__main__':
    sys.exit(main())
