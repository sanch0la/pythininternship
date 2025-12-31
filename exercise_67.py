""""
Ask the user to enter numbers until they enter 0.
Compute and print the total sum.
"""
import sys


def main():
    number = int(input("Enter a number: "))
    total = 0

    while number != 0:
        total += number
        number = int(input("Enter a number: "))
    print(f"The total is {total}")


    return 0


if __name__ == '__main__':
    sys.exit(main())
