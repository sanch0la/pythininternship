""""
Ask the user for five words.
Store them in a list: `words`.
Then construct a new list `a_words` containing only those words that begin with "a" or "A".

Constraint:
You may not use any loop.
You may only use:
indexing
slicing
boolean expressions
list comprehensions
empty list initialisation
Example strategy: check each element individually and build the result list step-by-step.
"""

import sys


def main():
    word1 = input("Enter a first word: ")
    word2 = input("Enter second word: ")
    word3 = input("Enter a third word: ")
    word4 = input("Enter a fourth word: ")
    word5 = input("Enter a fifth word: ")

    words = [word1, word2, word3, word4, word5]
    print(f"words: {words}")

    a_words = []

    (words[0][:1] == "a" or words[0][:1] == "A") and a_words.append(words[0])
    (words[1][:1] == "a" or words[1][:1] == "A") and a_words.append(words[1])
    (words[2][:1] == "a" or words[2][:1] == "A") and a_words.append(words[2])
    (words[3][:1] == "a" or words[3][:1] == "A") and a_words.append(words[3])
    (words[4][:1] == "a" or words[4][:1] == "A") and a_words.append(words[4])
    print(f"a_words new list is : {a_words}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
