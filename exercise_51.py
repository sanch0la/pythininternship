""""
Given:

rates = {
    "USD": 160.0,
    "EUR": 170.0,
    "GBP": 200.0

}

Ask the user for a currency code.

If the code exists in the dictionary, print the rate.

Otherwise, print "Currency not supported".
"""
import sys


def main():
    rates = {"USD": 160.0, "EUR": 170.0, "GBP": 200.0}
    currency_mode = input("Enter a currency code: ")
    if currency_mode in rates:
        print(rates[currency_mode])
    else:
        print("Currency not supported")

    return 0


if __name__ == '__main__':
    sys.exit(main())
