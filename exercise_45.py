""""
Ask the user for their age.

If the age is at least 18, print "Adult".

Otherwise, print "Minor".
"""
import sys


def main():
    try:
        age = int(input("Age: "))

        if age >= 18:
            print("Adult")
        else:
            print("Minor")
    except ValueError:
        print("Not an integer")


        return 0

if __name__ == '__main__':
    sys.exit(main())
