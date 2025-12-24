"""
Ask the user for:
name
birth year (integer)
country
Store them in a dictionary profile.

Then create a new dictionary summary with:
"NAME" → uppercase name
"age_in_2025" → 2025 - birth_year
"country" → lowercase country
Print both dictionaries with labels.
"""
import sys


def main():
    name = input("Enter a name: ")
    birth_year = int(input("Enter a birth year: "))
    country = input("Enter a country: ")


    profile = {"NAME": name, "birth_year": birth_year, "country": country}
    print(profile)

    profile["NAME"] = name.upper()
    profile["age_in_2025"] = 2025 - birth_year
    profile["country"] = country.lower()

    profile2 = {"NAME": name.upper(), "birth_year": 2025 - birth_year, "country": country.lower()}

    print(profile2)
    return 0


if __name__ == '__main__':
    sys.exit(main())