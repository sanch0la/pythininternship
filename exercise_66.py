""""
Ask the user repeatedly for input until they enter "quit".
Print each input except "quit".
"""
import sys


def main():
    user_input = input("Enter a word: ")
    while user_input != "quit":
        print(user_input)
        user_input = input("Enter a word: ")

    return 0


if __name__ == '__main__':
    sys.exit(main())
