"""
Ask the user for a value using input().

If the input is empty, print "No input provided".

Else if the input is numeric, print "Numeric input".

Else print "Text input".

Constraints:
No loops
No exception handling
Use:
.isdigit()
truthiness of strings
if / elif / else
"""
import sys


def main():
    value = input("Enter an input: ")
    if not value:
        print("No input provided")
    elif value.isdigit():
        print("Numeric input")
    else:
        print("Text input")
    return 0


if __name__ == '__main__':
    sys.exit(main())
