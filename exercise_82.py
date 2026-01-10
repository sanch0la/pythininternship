"""
Rewrite double_number(n) so it returns the result instead of printing it.
Print the returned value outside the function.
"""
import sys


def main():
    def double_number(n):
        return n * 2

    print(double_number(2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
