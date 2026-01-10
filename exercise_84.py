"""
Define a function describe_person(name, age) that:
prints a sentence
returns the age next year
"""
import sys


def main():
    def describe_person(name, age):
        age_next_year = age + 1
        print(f"{name} is {age} years old now and will be {age_next_year} years old next year.")
        return age_next_year
    describe_person("John", 29)

    return 0


if __name__ == '__main__':
    sys.exit(main())