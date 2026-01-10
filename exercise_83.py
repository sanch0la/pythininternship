"""
Write a function that:
prints a message
returns None
Assign the result to a variable and print it.
"""
import sys


def main():
    def print_message():
        print('Hello World!')
        return None

    message = print_message()
    print(message)

    return 0


if __name__ == '__main__':
    sys.exit(main())
