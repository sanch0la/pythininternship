""""
Given a list of banned words, check whether any appear in a user-provided message.
Stop checking as soon as one is found.
"""
import sys


def main():
    sentence = input("Enter a sentence: ")
    banned_words = ["my", "name", "is", "Jordan", "and", "I", 'am']
    found_banned_words = False

    for word in banned_words:
        if word in sentence:
            found_banned_words = True
        print("Banned word found:", found_banned_words)

        break
    return 0


if __name__ == '__main__':
    sys.exit(main())
