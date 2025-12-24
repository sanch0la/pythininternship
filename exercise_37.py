""""
data = {"a": 1, "b": 2, "c": 3}


Print the number of key–value pairs
"""
import sys


def main():
    data = {"a": 1, "b": 2, "c": 3}
    print(f"The number of key-value pairs is {len(data)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())