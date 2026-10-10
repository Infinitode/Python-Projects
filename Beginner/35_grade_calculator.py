"""Calculate an average and letter grade from a set of test scores."""


def calculate_grade(scores):
    """Return (average, letter grade) for scores between 0 and 100."""
    if not scores or any(not 0 <= score <= 100 for score in scores):
        raise ValueError("Enter at least one score between 0 and 100.")

    average = sum(scores) / len(scores)
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    return average, letter


def main():
    print("Grade Calculator (press Enter after your last score)")
    scores = []
    while True:
        try:
            answer = input("Score (0-100): ").strip()
        except EOFError:
            break
        if not answer:
            break
        try:
            score = float(answer)
        except ValueError:
            print("Please enter a number between 0 and 100.")
            continue
        if not 0 <= score <= 100:
            print("Please enter a number between 0 and 100.")
            continue
        scores.append(score)

    if not scores:
        print("No scores entered.")
        return
    average, letter = calculate_grade(scores)
    print("Average: {:.2f} | Letter grade: {}".format(average, letter))


if __name__ == "__main__":
    main()
