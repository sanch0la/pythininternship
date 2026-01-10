import sys


def main():
    school = ["Books","pens","pupils","Uniform", "tie"]
    for i in range(len(school)):
        print(f"{i} ==> {school[i]}")


if __name__ == '__main__':
    sys.exit(main())