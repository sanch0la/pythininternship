import sys


def main():
    banned_words = ["spam", "scam", "fake"]
    message = input("Enter your message: ")

    found = False

    for word in banned_words:
        if word in message:
            found = True
            break

    print("Banned word found:", found)

    return 0


if __name__ == '__main__':
    sys.exit(main())