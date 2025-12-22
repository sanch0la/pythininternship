""""
Given "values = [5, 6, 7, 8]", create "first_two" containing only the first two items using slicing
"""
import sys


def main():
    values = [5, 6, 7, 8]
    print(f"values is {values}")

    first_two = values[:2]
    print(f"first_two is {first_two}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
