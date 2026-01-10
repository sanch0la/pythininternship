""""
Define add(a, b) that returns their sum.
Call it using positional arguments.
"""
import sys


def main():
    def add(a, b):
        print(a + b)

    add(80, 2)
    return 0


if __name__ == '__main__':
    sys.exit(main())
