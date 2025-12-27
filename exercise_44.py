""""
Ask the user for a word.

If the word is exactly "python", print "Correct word".
"""
import sys


def main():
    word = input("Enter a word: ")
    if word == "python":
        print("Correct word")
    else:
        print("Incorrect word")

    return 0


if __name__ == '__main__':
    sys.exit(main())