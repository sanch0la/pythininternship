import sys

def main():
    age  = int(input("Enter your age: "))
    if age.is_integer() == False:
        print("Invalid input")
    else:
        age = int(age)

    if age >= 18:
        print("True")
    else:
        print("False")

    return 0

if __name__ == "__main__":
    sys.exit(main())