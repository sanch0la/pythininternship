"""
a) Function to compute monthly repayment
b) Function to compute total repayment
c) Print a summary using both
"""
import sys


def main():
    principal = int(input("Enter the principal: "))
    rate = int(input("Enter the interest: "))
    time = int(input("Enter the time: "))

    def monthly_repayment(principal, rate, time):
        simple_interest = principal * (rate / 100) * (time / 12)
        monthly_payment = simple_interest + (principal / time)
        return monthly_payment

    print(f"Your monthly repayment is {monthly_repayment(principal, rate, time)}")

    def total_repayment(principal, rate, time):
        simple_interest = principal * (rate / 100) * (time / 12)
        monthly_payment = simple_interest + (principal / time)
        total_repayment = monthly_payment * time
        return total_repayment

    print(f"The total repayment is {total_repayment(principal, rate, time)}")

    print(
        "SUMMARY\n"
        f"Your monthly repayment is {monthly_repayment(principal, rate, time)}\n"
        f"Your total repayment is {total_repayment(principal, rate, time)}"
    )

    return 0


if __name__ == '__main__':
    sys.exit(main())
