""""
Change the value of age in the dictionary to 26.

Print the updated dictionary.
"""
import sys


def main():

    person = {"name": "Alice", "age": 25, "country": "Kenya"}
    person["age"] = 26
    print(f"The person's new age is {person["age"]}")
    return 0


if __name__ == '__main__':
    sys.exit(main())