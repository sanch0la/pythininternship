"""
Create a list of six integers: [10, 20, 30, 40, 50, 60].
Using only slicing and concatenation (no loops), construct a new list containing the middle four numbers.
"""
import sys


def main():
    integers = [10, 20, 30, 40, 50, 60]
    print("Initial list:", integers)

    new_list = integers[1:5]
    print("New list is :", new_list)
    return 0


if __name__ == '__main__':
    sys.exit(main())
