import sys

def main():
    x = int(input("Enter a number x:"))
    y = int(input("Enter a number y:"))

    print(f"{x} divide by {y} = {x/y}")
    print(f"The integer division of {x} by y is {x//y}")
    print(f"The remainder of {x} divided by {y} is {x%y}")


    return 0
if __name__ == "__main__":
    sys.exit(main())
