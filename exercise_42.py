"""
grades = {
    "A": 80,
    "B": 70,
    "C": 60,
    "D": 50
}

Ask the user for a grade letter (A, B, C, or D).
Print the corresponding minimum score.
"""
import sys


def main():
    grades = {"A": 80, "B": 70, "C": 60, "D": 50}
    grade_letter = input("Enter a grade letter: ").upper()

    if grade_letter in grades:
        print(grades[grade_letter])
    else:
        print("Invalid grade")
    return 0


if __name__ == '__main__':
    sys.exit(main())
