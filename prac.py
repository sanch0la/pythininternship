import sys


def main():
    highest_score = -1
    top_name = ""

    # Open the file safely
    with open("scores.txt", "r") as file:
        first_line = True

        # Iterate over each line
        for line in file:
            if first_line:
                first_line = False
                continue  # skip header

            # Extract name and score
            parts = line.strip().split(",")
            name = parts[0]
            score = int(parts[1])  # numeric conversion

            # Track highest score
            if score > highest_score:
                highest_score = score
                top_name = name

    # Print result
    print("Top scorer:", top_name)
    print("Highest score:", highest_score)

    return 0


if __name__ == '__main__':
    sys.exit(main())