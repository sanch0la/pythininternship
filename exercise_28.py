""""
Ask the user to enter four integers.
Store them in 'nums'.
Replace:
the first number with its square.
the last number with its cube.
The compute and print the sum of all four numbers.

"""
import sys


def main():
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        number3 = int(input("Enter the third number: "))
        number4 = int(input("Enter the fourth number: "))

    except ValueError:
        print("Please enter a number.")
        return 0

    nums = [number1, number2, number3, number4]

    nums[0] = nums[0] ** 2
    nums[-1] = nums[-1] ** 2

    sum_nums = sum(nums)
    print(nums)
    print(f"The sum of nums is {sum_nums}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
