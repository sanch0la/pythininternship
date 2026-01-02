""""
Given:

stock = {"pen": 10, "book": 0, "eraser": 5}

Print only the items that are out of stock.

"""
import sys


def main():
    stock = {"pen": 10, "book": 0, "eraser": 5}

    for item in stock:
        if stock[item] == 0:
            print(f"{item} is out of stock")
    return 0


if __name__ == '__main__':
    sys.exit(main())