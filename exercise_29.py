""""
Ask the user for:
their name (string)
their age (integer)
their country (string)
Store the results in a list 'profile = [name, age, country]'.

Then produce a new list:
'summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]'.

Finally print both lists with clear labels.

"""

import sys


def main():
    try:
        name = input("What is your name? ")
        age = int(input("What is your age? "))
        country = input("What is your country? ")
    except ValueError:
        print("Sorry, I didn't understand your input.")
        return 0
    profile = [name, age, country]

    print(profile)

    summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]
    print(summary)

    return 0


if __name__ == '__main__':
    sys.exit(main())
