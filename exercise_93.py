""""
Define a function that takes a list of numbers and returns their total.
"""
import sys


def main():
    def list_of_numbers():
        x = [1, 3, 4, 56, 7, 8, 5, 34]
        print(f"The total for {x} is {sum(x)}")

    list_of_numbers()
    return 0


if __name__ == '__main__':
    sys.exit(main())
