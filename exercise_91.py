""""
Define grade_label(score) that returns "Pass" or "Fail".
"""
import sys


def main():
    def grade_label(score):
        if score >= 40:
            return "Pass"
        else:
            return "Fail"
    grade_label(49)
    print(grade_label(49))
    return 0


if __name__ == '__main__':
    sys.exit(main())