import sys


def main():
    grades = {
        "A": 80,
        "B": 70,
        "C": 60,
        "D": 50
    }

    grade = input("Enter a grade letter (A, B, C, or D): ").upper()

    if grade in grades:
        print(f"The minimum score for grade {grade} is {grades[grade]}")
    else:
        print("Invalid grade letter.")

    return 0


if __name__ == '__main__':
    sys.exit(main())