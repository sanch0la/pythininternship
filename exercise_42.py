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
    grade_letter = input("Enter a grade letter: ")
    print(grades[grade_letter])
    try:
        if grades == "A":
         print(80)
        elif grades == "B":
         print(70)
        elif grades == "C":
            print(60)
        elif grades == "D":
            print(50)
    except :
         print("Invalid grade")



    return 0


if __name__ == '__main__':
    sys.exit(main())
