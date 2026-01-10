""""

Given the attached file scores.txt where each line contains:

name,score

Your program should:
Open the file safely
Iterate over each line
Extract names and scores
Track:
highest score
corresponding name
Print the top scorer
Constraints:
Use split()
Use numeric conversion
Use compound assignment e.g., += or -= or /= (a combination of an assignment with another operator)
No functions
"""

import sys


def main():
    highest_score = -1


    with open("scores.txt") as f:
        for row in f:

            individual = row.strip().split()
            print(individual)
            name = individual[0]
            score = int(individual[1])

    if score > highest_score:
        highest_score = score
        print(highest_score)

    return 0


if __name__ == '__main__':
    sys.exit(main())
