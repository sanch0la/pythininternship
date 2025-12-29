""""
Ask the user for a list of three words (build a list manually).

If the list is non-empty, print "List has items".

Else print "Empty list".
"""
import sys


def main():
    words = input(f"Enter three words: ")
    print(words)
    if len(words) > 1:
        print("List has items")
    else:
        print("Empty list")
        return 0


if __name__ == '__main__':
    sys.exit(main())