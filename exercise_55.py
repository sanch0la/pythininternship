""""
Ask the user for:
name
three test scores (integers)
Store the data in a dictionary:

student = {
    "name": ...,
    "scores": [...],

}

Compute the average score and add it to the dictionary.

Then:
If the average is ≥ 70, status is "Pass"
If the average is ≥ 50 and < 70, status is "Supplementary"
Otherwise, status is "Fail"
Add "status" to the dictionary and print the final record neatly.

Constraints:
Must use if / elif / else
Must use and
Must use compound assignment at least once
Must reuse Week 1–3 ideas (lists, dicts, arithmetic)
"""
import sys


def main():
    name = input("What is your name? ")
    try:
        test_score1 = int(input("What is your test score 1? "))
        test_score2 = int(input("What is your test score 2? "))
        test_score3 = int(input("What is your test score 3? "))

        average_score = (test_score1 + test_score2 + test_score3) / 3
        if average_score >= 70:
            status = "Pass"
        elif average_score >= 50 and average_score < 70:
            status = "Supplementary"
        else:
            status = "Fail"

        student = {
            "name": name,
            "scores": [test_score1, test_score2, test_score3],
            "average_score": average_score,
            "status": status,
        }
        print(student)
    except ValueError:
        print("Please enter a number.")

        return 0


if __name__ == '__main__':
    sys.exit(main())
