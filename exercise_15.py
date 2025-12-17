"""
Ask for a word. Print whether the word starts with "a" or "A" using a boolean expression.
"""

import sys


def main():
    word = input("Enter a word: ")
    if word[0] == "a":
        print("True")
    elif word[0] == "A":
        print("False")
    else:
        while word[0] != "a" or word[0] != "A":
            word  = input("Retype the word: ")
            if word[0] == "a":
                print("True")
            elif word[0] == "A":
                print("False")
            break

    return 0


if __name__ == '__main__':
    sys.exit(main())
