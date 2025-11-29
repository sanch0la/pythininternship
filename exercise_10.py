import sys

def main():

    x = int(input("Enter a number x:"))
    y = float(input("Enter a number y:"))

    if type(x) != int or type(y) != float:
        print ("Invalid type inputs")

    print(f"The integer is {x}", )
    print(f"The float is {y}")

    return 0

if __name__ == "__main__":
    sys.exit(main())