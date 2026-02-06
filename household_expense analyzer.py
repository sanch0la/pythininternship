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


def read_file():
    with open("expense.txt") as f:
        for line in f:
            print(line)


read_file()


def categorize_items():
    categories = {}

    with open("expense.txt", "r") as f:
        for line in f:

            parts = line.strip().split(",")

            if len(parts) == 2:
                category = parts[0].strip()
            try:
                amount = float(parts[1].strip())

                categories[category] = categories.get(category, 0.0) + amount
            except ValueError:
                print(f"Skipping invalid amount on line: {line.strip()}")

        print("Final Totals by Category:")
        print(categories)
        return categories


categorize_items()


def overall_expenditure(categories):
    total_expenditure = sum(categories.values())
    return total_expenditure


my_categories = categorize_items()
my_overall_expenditure = overall_expenditure(my_categories)
print(f"Overall Expenditure: {my_overall_expenditure}")


def highest_spending(categories):
    highest_category = max(categories, key=categories.get)
    return highest_category


my_highest_spending = highest_spending(my_categories)
print(f"Highest Spending: {my_highest_spending}")


def main():
    # Calculate the values
    my_categories = categorize_items()
    total = overall_expenditure(my_categories)
    top_cat = highest_spending(my_categories)

    # Print the Summary
    print("\n" + "=" * 30)
    print("      EXPENSE SUMMARY")
    print("=" * 30)
    print(f"Total Categories:  {len(my_categories)}")
    print(f"Total Spent:       ${total}")
    print(f"Highest Category:  {top_cat} (${my_categories[top_cat]})")
    print("=" * 30)

    return 0


if __name__ == '__main__':
    sys.exit(main())
