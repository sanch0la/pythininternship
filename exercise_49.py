""""
Given:

colors = ["red", "green", "blue"]

Ask the user for a color.

If the color is in the list, print "Color available", else print "Color not found".
"""
import sys


def main():
    colors = ["red", "green", "blue"]
    color1 = input('Enter a color: ')
    if color1 in colors:
        print("Color available")
    else:
        print("Color not found")
    return 0


if __name__ == '__main__':
    sys.exit(main())