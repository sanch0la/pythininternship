""""
a) Write a function to compute simple interest
b) Write a function to compute total amount
c) Use both functions to compute interest from user input
"""
import sys


def main():
    def simple_interest(principal,rate, time):
        return principal*(rate/100)*time
    def total_amount(principal,interest):
        return principal + simple_interest(principal,interest,time)
    principal = float(input("Enter the principal: "))
    interest = float(input("Enter the interest: "))
    time = float(input("Enter the time: "))

    simple_interest(principal, interest, time)
    print(f"The simple interest is {simple_interest(principal, interest, time)}")
    print(f"The total amount is {total_amount(principal, interest)}")
    total_amount(principal, interest)






    return 0


if __name__ == '__main__':
    sys.exit(main())