"""
Ask the user for five numbers, store them in a list.
Using the sorted() function and a for-construct, print the numbers in ascending order without modifying the original list.
"""
import sys


def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    number4 = int(input("Enter the fourth number: "))
    number5 = int(input("Enter the fifth number: "))

    number = [number1, number2, number3, number4, number5]
    for num in number:
        number.sort()
    print(number)
    return 0


if __name__ == '__main__':
    sys.exit(main())
