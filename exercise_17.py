"""
Call print() on a message and assign it to a variable:

v = print("Hello")

Print v and observe its value.
"""

import sys


def main():
    v = print("My name is Jordan")
    print(v)
    return 0


if __name__ == '__main__':
    sys.exit(main())
