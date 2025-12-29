"""
Ask the user for:
a username
a boolean flag "is_admin" (True/False)
Given:

access_level = 1

If the user is "admin" or is_admin is True, increase access_level by 4.

Otherwise, increase it by 1.

Print the final access level.

"""
import sys


def main():
    username = input("Enter username: ")
    is_admin = input("Is admin? : ")

    access_level = 1
    if is_admin == "True":
        access_level += 4
    else:
        access_level += 1

    print(f" Final access level: {access_level}")
    return 0


if __name__ == '__main__':
    sys.exit(main())