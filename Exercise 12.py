import sys

def main():

    number = int(input("Enter a number: "))
    word = input("Enter a word: ")

    print(f"{word} repeated {number} times")

    return 0
if __name__ == "__main__":
    sys.exit(main())