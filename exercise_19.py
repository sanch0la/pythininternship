import sys
""""
Ask the user for three words (one per input).

Store them in a list and print the list exactly as Python represents it.
"""

def main():
    word1  = input("Enter your first word: ")
    word2 = input("Enter your second word: ")
    word3 = input("Enter your third word: ")

    print([word1, word2, word3])
    return 0


if __name__ == '__main__':
    sys.exit(main())