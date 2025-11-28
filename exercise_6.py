import sys

def main():
    x = 10

    x += 10
    print(x)
    x -= 10
    print(x)
    x *= 10
    print(x)
    x **= 10
    print(x)

    return 0

if __name__ == '__main__':
    sys.exit(main())