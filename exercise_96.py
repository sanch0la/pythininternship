""""
a) Function to compute average score
b) Function to assign grade label
c) Apply both to a list of scores
"""
import sys
from wsgiref.util import request_uri


def main():
    score1 = int(input("Enter score 1: "))
    score2 = int(input("Enter score 2: "))
    score3 = int(input("Enter score 3: "))
    score4 = int(input("Enter score 4: "))
    score5 = int(input("Enter score 5: "))

    scores = [score1, score2, score3, score4, score5]

    def average_score(scores):
        average_score = sum(scores) / len(scores)
        return average_score

    average_score(scores)
    print(f"The average score is {average_score(scores)}")

    def grade_label(scores):
        average_score = sum(scores) / len(scores)
        if average_score > 70:
            return "A"
        elif 70 > average_score > 60:
            return "B"
        elif 60 > average_score > 50:
            return "C"
        elif 50 > average_score > 40:
            return "D"
        else:
            return "E"

    grade_label(scores)
    print(f"The grade is {grade_label(scores)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
