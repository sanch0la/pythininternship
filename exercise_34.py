""""
Ask the user for:

their name
their age (convert to int)
their city
Store the data in a dictionary called profile.



Print profile.



Part B


Add a new key age_next_year whose value is the user’s age plus one.

Print the updated dictionary.

"""
import sys


def main():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    city = input("What is your city? ")

    profile = {"name": name, "age": age, "city": city}
    print(profile)

    profile["age_next_year"] = age + 1
    print(profile)
    return 0


if __name__ == '__main__':
    sys.exit(main())