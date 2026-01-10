"""
Define greet(name, greeting="Hello").
Call it with and without the greeting argument.
"""
import sys


def main():
    def greet(name, greeting="Hello"):
        print(f"{greeting} {name}")

    greet(name="John", greeting="Hello")
    greet('John')
    return 0


if __name__ == '__main__':
    sys.exit(main())
