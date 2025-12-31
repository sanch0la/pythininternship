""""
i = 0
while i < 5:
    print(i)
    i += 1 # statement that modifies i

Over to you: Use a while loop to print numbers from 5 to 1 so that your program produces the following output:

5
4
3
2
1

Bonus question: What happens if the suite does not include a statement that modifies the variable in the assignment expression? Try it!
"""
import sys


def main():
    i = 5
    while i >= 1:
        print(i)
        i -= 1


    return 0


if __name__ == '__main__':
    sys.exit(main())