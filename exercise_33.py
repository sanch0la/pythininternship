""""
Add a new key is_student with value False.

Print the dictionary.

"""
import sys


def main():
    person = {"name": "Alice", "age": 25, "country": "Kenya"}
    person["is_student"] = False
    print(person)
    return 0


if __name__ == '__main__':
    sys.exit(main())