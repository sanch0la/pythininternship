""""
Using the same list from Exercise 56, compute and print the total sum.
"""


import sys


def main():
    numbers = [10, 20, 30, 40]
    sum = numbers[0] + numbers[1] + numbers[2] + numbers[3]
    print(sum)
    return 0


if __name__ == '__main__':
    sys.exit(main())