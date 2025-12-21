""""
Ask the user for three numbers as strings (e.g., "12", "5", "100").
Store them in a list.
Then convert each element to an int *without loops* (explicit index assignments only).
Finally, compute and print their total.
"""

import sys


def main():
    number = (input("Enter first number: "))
    number1 = (input("Enter second number: "))
    number2 = (input("Enter third number: "))

    list_of_numbers = [number, number1, number2]
    print(list_of_numbers)

    list_of_numbers[0] = int(list_of_numbers[0])
    list_of_numbers[1] = int(list_of_numbers[1])
    list_of_numbers[2] = int(list_of_numbers[2])

    list_of_new_numbers = (list_of_numbers[0], list_of_numbers[1], list_of_numbers[2])

    total = list_of_new_numbers[0] + list_of_new_numbers[1] + list_of_new_numbers[2]

    print(list_of_new_numbers)
    print(f"Total is {total}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
