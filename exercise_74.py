""""
Ask the user for five numbers.
As each number is entered, print the current maximum so far.
"""
import sys


def main():
    number1 = int(input("Enter the first number: "))
    print(f"{number1} is the current maximum so far.")

    number2 = int(input("Enter the second number: "))
    if number2 > number1:
        print(f"{number2} is the current maximum so far.")
    else:
        print(number1)
    number3 = int(input("Enter the third number: "))
    if number3 > number2 and number3 > number1:
        print(f"{number3} is the current maximum so far.")
    else:
        pass
    number4 = int(input("Enter the fourth number: "))
    if number4 > number1 and number4 > number2 and number4 > number3:
        print(f"{number4} is the current maximum so far.")
    number5 = int(input("Enter the fifth number: "))
    if number5 > number1 and number5 > number2 and number5 > number3 and number5 > number4:
        print(f"{number5} is the current maximum so far.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
