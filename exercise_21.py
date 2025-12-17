import sys
""""
Replace the second word in the list with string "UPDATED". Print the new list.
"""


def main():
    words = ["Jordan" ,"Olwalo" ,'Kisera']

    words[1] = "UPDATED"
    print(words)

    return 0


if __name__ == '__main__':
    sys.exit(main())