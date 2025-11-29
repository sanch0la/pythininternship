import sys

def main():

    x = int(input("Enter a number x:"))
    y= float(x)

    print(f"The integer is {x}", )
    print(f"The float is {y}")

    if type(y) != float:
        print("The type is not float")

    return 0

if __name__ == "__main__":
    sys.exit(main())