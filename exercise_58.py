import sys


def main():
    word = input('Enter a word: ')
    for character in word:
        print(character)
    return 0


if __name__ == '__main__':
    sys.exit(main())