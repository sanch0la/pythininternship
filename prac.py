import sys
from operator import index, indexOf


def main():
    for number in range(1, 100):
        if number % 7 == 0 or number % 11 == 0:
            print(number)
    return 0

if __name__ == '__main__':
    sys.exit(main())
