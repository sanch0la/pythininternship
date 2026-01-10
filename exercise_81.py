""""
Inside a function, define a variable x = 10.
Outside the function, try to print x.
Observe and explain what happens (comment).
"""
import sys


def main():
    def trial_x():
        x = 10

    trial_x()
    return 0

# The output is blank. It just displays that the process finishes with an exit code of 0
if __name__ == '__main__':
    sys.exit(main())
