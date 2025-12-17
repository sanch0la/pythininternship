import sys


def main():
    word = input("Enter a word: ")
    print(word.startswith("a") or word.startswith("A"))


    return 0


if __name__ == '__main__':
    sys.exit(main())