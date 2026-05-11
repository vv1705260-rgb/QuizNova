SCORE_FILE = "scores.txt"

# Save Score
def save_score(name, score):

    with open(SCORE_FILE, "a") as file:
        file.write(f"{name},{score}\n")

# Display Scores
def display_top_scores():

    try:
        with open(SCORE_FILE, "r") as file:

            scores = []

            for line in file:
                name, score = line.strip().split(",")
                scores.append((name, int(score)))

            scores.sort(key=lambda x: x[1], reverse=True)

            for rank, (name, score) in enumerate(scores[:5], start=1):
                print(f"{rank}. {name} - {score}")

    except FileNotFoundError:
        print("No scores available yet.")
