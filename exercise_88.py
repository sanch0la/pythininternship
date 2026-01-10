""""
Call the same function using keyword arguments in reversed order.
"""
import sys


def main():
    def add(a, b):
        print(a + b)

    add(b=80, a=2)
    return 0


if __name__ == '__main__':
    sys.exit(main())
