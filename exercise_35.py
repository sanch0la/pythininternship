""""
Part A


Ask the user for:

student name
three test scores (integers)
Store the scores in a list.






Part B


Create a dictionary called student with keys:

"name" → student name
"scores" → list of scores
Print the dictionary.






Part C


Compute the average score and add a new key:

"average" → average score (float)
Print the final dictionary.

"""
import sys


def main():
    name = input("Enter your name: ")
    score1 = int(input("Enter your score1: "))
    score2 = int(input("Enter your score2: "))
    score3 = int(input("Enter your score3: "))

    scores = [score1, score2, score3]
    print(name, scores)

    student = {"name": name, "scores": scores}
    print(student)

    average_score = sum(scores) / len(scores)
    student["average_score"] = average_score
    print(student)
    return 0


if __name__ == '__main__':
    sys.exit(main())