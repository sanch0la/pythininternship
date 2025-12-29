""""
Ask the user for an optional middle name.

If the input is empty, set middle_name = None.

If middle_name is not None, print the full name with middle name.

Else print only first and last name.
"""
import sys


def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    middle_name = input(f"Enter optional middle name: ")
    if middle_name == 0:
        middle_name = None
    elif middle_name is not None:
        print(f"The full name is {first_name} {middle_name} {last_name}")

    else:

        print(f"The full name is {first_name} {last_name}")
    return 0


if __name__ == '__main__':
    sys.exit(main())