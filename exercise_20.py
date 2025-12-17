import sys
""""

Using the list created in Exercise 19, print:
the first word
the last word
the length of the list
"""

def main():
    words = ["Jordan" , "Olwalo" , "Kisera"]
    print(words[0])
    print(words[-1])
    print(f"The length of the list is {len(words)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())