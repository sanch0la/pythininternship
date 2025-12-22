""""
Given "items = [10, 20, 30]", crate an independent copy using slicing and print both lists.
"""
import sys


def main():
    items = [10, 20, 30]
    print(f"items is {items}")

    independent_copy = items[:]
    print(f"The independent_copy is {independent_copy}")
    return 0


if __name__ == '__main__':
    sys.exit(main())