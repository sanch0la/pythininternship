""""
a) Function to sum transaction values
b) Function to apply tax
c) Produce final total
"""
import sys


def main():
    transactions = [800, 1000, 200, 430, 647, 389]

    def sum_transactions(transactions):
        total = sum(transactions)
        return total

    sum_transactions(transactions)
    print(f"The sum of all transactions is {sum_transactions(transactions)}")

    def apply_tax(transactions):
        total = sum(transactions)
        tax = 0.16 * total
        return tax

    print(f"The tax is {apply_tax(transactions)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
