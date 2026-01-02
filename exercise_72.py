""""
Ask the user for a sentence.
Print only the words longer than 4 characters.
"""
import sys


def main():
    sentence = input("Enter a sentence: ")
    for word in sentence.split():
        if len(word) >= 4:
            print(word)

    return 0


if __name__ == '__main__':
    sys.exit(main())