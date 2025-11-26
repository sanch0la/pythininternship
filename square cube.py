import sys

def main():
    x=int(input("Enter a number x:"))
    y = pow(x,2 )
    z = pow(x,3)
    print(f"The square of {x} is {y} and its cube is {z} ")



    return 0
if __name__ == "__main__":
    sys.exit(main())