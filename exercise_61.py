""""
Using the same dictionary from Exercise 60, print each value.
"""
import sys


def main():
    person = {"name": "Alice", "age": 30, "city": "Nairobi"}
    for key,value in person.items():
        print(value)
    return 0


if __name__ == '__main__':
    sys.exit(main())