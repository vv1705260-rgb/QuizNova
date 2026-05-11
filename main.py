import time
from questions import quiz_questions
from scoreboard import save_score, display_top_scores
from utils import clear_screen, loading_animation

player_name = input("Enter Your Name: ")

score = 0
correct_answers = 0
wrong_answers = 0

clear_screen()

print("=" * 60)
print("        ADVANCED PYTHON QUIZ GAME")
print("=" * 60)

loading_animation()

for index, q in enumerate(quiz_questions, start=1):

    print(f"\nQuestion {index}: {q['question']}")
    print("-" * 50)

    for option in q['options']:
        print(option)

    answer = input("\nEnter option (A/B/C/D): ").upper()

    if answer == q['answer']:
        print("✅ Correct Answer!")
        score += 10
        correct_answers += 1
    else:
        print(f"❌ Wrong! Correct Answer: {q['answer']}")
        wrong_answers += 1

    time.sleep(1)
# Quiz Questions Loop
for index, q in enumerate(quiz_questions, start=1):

    print(f"\nQuestion {index}: {q['question']}")
    print("-" * 50)

    for option in q['options']:
        print(option)

    answer = input("\nEnter option (A/B/C/D): ").upper()

    # Correct Answer Check
    if answer == q['answer']:

        print("\n✅ Correct Answer!")
        print(f"✔ Correct Option : {q['answer']}")
        print(f"📘 Answer : {q['correct_text']}")

        score += 10
        correct_answers += 1

    else:

        print("\n❌ Wrong Answer!")
        print(f"✔ Correct Option : {q['answer']}")
        print(f"📘 Correct Answer : {q['correct_text']}")

        wrong_answers += 1

    print("\n⏳ Moving to next question...")
    time.sleep(2)
# Result Section
clear_screen()

print("=" * 60)
print("                 QUIZ RESULT")
print("=" * 60)

print(f"👤 Player Name      : {player_name}")
print(f"🏆 Final Score      : {score}")
print(f"✅ Correct Answers  : {correct_answers}")
print(f"❌ Wrong Answers    : {wrong_answers}")

percentage = (correct_answers / len(quiz_questions)) * 100

print(f"📊 Percentage       : {percentage:.2f}%")

if percentage >= 80:
    print("🌟 Excellent Performance!")
elif percentage >= 50:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")

# Save Score
save_score(player_name, score)

# Display Leaderboard
print("\n🏅 LEADERBOARD")
display_top_scores()

print("\n🎉 Thank You For Playing!")
