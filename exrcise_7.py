import sys

def main():
    word = input("Enter your name: ")

    if word == '':
        print("No name entered")

    print(word[0])
    print (word[-1])

    return 0

if __name__ == "__main__":
    sys.exit(main())