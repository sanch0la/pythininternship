""""
You are given a file scores.txt.

a) Function to read scores into a dictionary
b) Function to compute averages
c) Function to classify students
d) Main program to print summaries

Constraints:
No global variables
Clear separation of responsibilities
"""
import sys


def main():
    def read_scores(scores):
        scores = {}
        with open("scores.txt") as f:
            for line in f:
                parts = line.strip().split(',')
                score = int(parts[-1].strip())

                scores[parts[0].strip()] = score

        print(scores.values())

    read_scores(read_scores)

    def compute_averages(scores):
        score_list = []
        with open("scores.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                score = parts[-1].strip()
                score_list.append(int(score))
        average = sum(score_list) / len(score_list)
        print(f"The average score is {average}")

    compute_averages(read_scores)

    def classify_students(scores):

        scores_dict = {}

        with open("scores.txt") as f:
            for line in f:
                parts = line.strip().split(',')
                name = parts[0].strip()
                score = int(parts[-1].strip())
                scores_dict[name] = score

        for name, score in scores_dict.items():
            if score >= 80:
                grade = "Grade A"
            elif 80 > score >= 60:
                grade = "Grade B"
            elif 60 > score >= 40:
                grade = "Grade C"
            else:
                grade = "D. Fail"

            print(f"{name}: {score} ({grade})")

    classify_students(read_scores)
    return 0


if __name__ == '__main__':
    sys.exit(main())
