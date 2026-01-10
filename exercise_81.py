""""
Inside a function, define a variable x = 10.
Outside the function, try to print x.
Observe and explain what happens (comment).
"""
import sys


def main():
    def trial_x():
        x = 10
    print(x)
    trial_x()


    return 0

# We get a name error. This is because we are printing x (The variable) outside the function block hence it
#it doesn't know whats happening outside this block
if __name__ == '__main__':
    sys.exit(main())
