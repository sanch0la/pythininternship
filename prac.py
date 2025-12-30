import sys


def main():
    words = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for word in range(len(words)):
        print(f"{word} == {words[word]}")
    return 0


if __name__ == '__main__':
    sys.exit(main())