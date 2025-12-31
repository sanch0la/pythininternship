""""
Using the word in Exercise 58, count how many characters it has using a loop (do not use len()).
"""
import sys


def main():
    word  = "Jordan"
    total = 0
    for character in word:
        total += 1
    print(f"The total character count is {total}")
    return 0


if __name__ == '__main__':
    sys.exit(main())