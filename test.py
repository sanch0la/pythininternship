import sys


def main():
    # Ask the user for five words
    words = [
        input("Enter word 1: "),
        input("Enter word 2: "),
        input("Enter word 3: "),
        input("Enter word 4: "),
        input("Enter word 5: ")
    ]

    # Construct a new list with words starting with 'a' or 'A'
    a_words = [w for w in words if w[:1] == "a" or w[:1] == "A"]

    print("Words starting with 'a' or 'A':", a_words)

    return 0


if __name__ == '__main__':
    sys.exit(main())