""""
Part A


Create a dictionary:
stats = {
    "count": 10,
    "average": 4.5,
    "valid": True

}


Print each value individually using key access.



Part B

Update:

"count" by increasing it by 5 using compound assignment
"valid" to False
Print the final dictionary.
"""
import sys


def main():
    stats = {"count": 10, "average": 4.5, "valid": True}
    print(stats["count"], stats["average"], stats["valid"])

    stats["count"] += 5
    stats["valid"] = False

    print(stats)

    return 0


if __name__ == '__main__':
    sys.exit(main())