import sys

def main():
    x = int(input("Enter the temperature of Nairobi: "))
    y = x*9/5 + 32
    print(f"The temperature of Nairobi in farenheit is {y} ")



    return 0
if __name__ == "__main__":
    sys.exit(main())