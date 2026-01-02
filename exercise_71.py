""""
Given a list of test scores:
compute the average
count how many are ≥ 50
compute the average for those that are ≥ 50
Print both results.
"""
import sys


def main():
    test_scores = [23, 24, 67, 74, 21, 13, 65, 35, 57, 86, 101]

    average1 = sum(test_scores) / len(test_scores)
    print(f"The first average is {average1}")

    total = [score for score in test_scores if score >= 50]
    print(f"The number of scores greater than 50 is {len(total)}")

    average2 = sum(total) / len(total)
    print(f"The second average score is {average2}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
