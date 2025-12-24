import sys


def main():
    x = int(input("x:"))
    y = 2 * x ** 4 + 3
    print(y)
    return 0


if __name__ == '__main__':
    sys.exit(main())