""""
Given any text file (you choose):

a) Function to read and normalize text (remove end of line characters)
b) Function to count words
c) Function to identify top N words
d) Print results neatly in a table
"""

import sys
import string
from collections import Counter


def read_and_normalize():
    with open("geek.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip().rstrip(string.punctuation)
        print(line)


def count_words():
    total_words = 0
    with open("geek.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip().rstrip(string.punctuation)
            words = line.split()
            total_words += len(words)

    print(f"The total number of words is {total_words} words.")


count_words()

read_and_normalize()


def get_top_words(n=3):
    all_words = []
    with open("geek.txt", "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            all_words.extend(clean_line.split())

    counts = Counter(all_words)
    return counts.most_common(n)


print(f"Top 3 words: {get_top_words(3)}")


def main():
    print("=" * 50)
    print("               EXECUTIVE SUMMARY              ")
    print(f"The total number of words is {count_words()}")
    print(f"The most common words are {get_top_words(3)}")
    print("=" * 50)

    return 0


if __name__ == '__main__':
    sys.exit(main())
