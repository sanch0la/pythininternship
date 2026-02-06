"""
You are given a file expenses.txt with:

category,amount

Your task is to write a program that:

a) Reads the file safely
b) Builds a dictionary of category totals
c) Computes overall expenditure
d) Identifies the highest-spending category
e) Prints a clear financial summary

Rules:
Must use at least four functions
No functions longer than ~15 lines
No global state i.e., no variables on the global scope that are referenced from the functions
All logic must be decomposed
"""
import sys


def get_categorized_data(filename):
    categories = {}

    with open(filename, "r") as f:

        next(f)
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                category = parts[0].strip()
                try:
                    amount = float(parts[1].strip())
                    categories[category] = categories.get(category, 0.0) + amount
                except ValueError:
                    print(f"Skipping invalid amount on line: {line.strip()}")
    return categories


def overall_expenditure(categories):
    return sum(categories.values())


def highest_spending(categories):
    return max(categories, key=categories.get)


def main():
    my_categories = get_categorized_data("expense.txt")

    total = overall_expenditure(my_categories)
    top_cat = highest_spending(my_categories)

    print("\n" + "=" * 50)
    print("      EXPENSE SUMMARY")

    print(f"Total Categories:  {len(my_categories)}")
    print(f"Total Spent:       ${total}")
    print(f"Highest Category:  {top_cat} (${my_categories[top_cat]})")
    print("=" * 30)

    return 0


if __name__ == '__main__':
    sys.exit(main())
