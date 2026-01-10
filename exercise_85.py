""""
Call the same function with three different inputs.
"""
import sys


def main():
    def describe_person(name, age):
        age_next_year = age + 1
        print(f"{name} is {age} years old now and will be {age_next_year} years old next year.")
        return age_next_year

    describe_person("John", 29)
    describe_person(name="John", age=29)
    person = describe_person("John", 29)
    print(person)

    return 0


if __name__ == '__main__':
    sys.exit(main())
