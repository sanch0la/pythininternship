""""
Ask the user for two integers a and b.

If both are positive, print "Both positive".

Otherwise, print "At least one is not positive".
"""
import sys


def main():
    while True:
        try:
            number_a = int(input("Enter a number a: "))
            number_b = int(input("Enter a number b: "))
            if number_a and number_b > 0:
                print("Both positive")
            else:
                print("At least one is not positive")
            break
        except ValueError:
            print("Please enter a number.")

    return 0


if __name__ == '__main__':
    sys.exit(main())
