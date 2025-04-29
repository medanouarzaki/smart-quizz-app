import json
import string
import random
import datetime
from colorama import Fore, Style, init
init(autoreset=True)
from inputimeout import inputimeout, TimeoutOccurred


# Utility: Clean text (remove spaces, punctuation, lowercase)
def clean(text):
    return text.strip().lower().translate(str.maketrans('', '', string.punctuation))

# Load questions from JSON
with open("questions.json", "r") as file:
    questions = json.load(file)

print(Fore.CYAN + "📚 Welcome to the Smart Quiz App!")
print("You can filter questions by category or difficulty.\n")

# Ask user for filters
selected_category = input("Enter a category to filter by (photography, Computer Science, Geography) (or press Enter to skip): ").strip().lower()
selected_difficulty = input("Enter difficulty (Easy, Medium, Hard) or press Enter to skip: ").strip().lower()

# Filter questions based on user input
filtered_questions = []
for q in questions:
    match_category = selected_category == "" or q["category"].lower() == selected_category
    match_difficulty = selected_difficulty == "" or q["difficulty"].lower() == selected_difficulty
    if match_category and match_difficulty:
        filtered_questions.append(q)

# Fallback if no questions match
if not filtered_questions:
    print("\n❗ No questions matched your filters. Showing all questions instead.\n")
    filtered_questions = questions

random.shuffle(filtered_questions)

# Start quiz
score = 0
for q in filtered_questions:
    try:
        user_answer = inputimeout(prompt=q["question"] + "\nYour answer (you have 10 seconds): ", timeout=10)
    except TimeoutOccurred:
        print(Fore.RED + "\n⏰ Time's up! You didn't answer in time.\n")
        user_answer = ""  

    cleaned_user = clean(user_answer)
    acceptable_answers = [clean(ans) for ans in q["answers"]]

    if cleaned_user in acceptable_answers:
        print(Fore.GREEN + "Correct!\n")
        score += 1
    else:
        print(Fore.RED + "Incorrect. Acceptable answers were:", ", ".join(q["answers"]), "\n")

# Final score
print(f"🎉 Quiz complete! You got {score} out of {len(filtered_questions)} correct.")

# Prepare score history data
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

score_entry = {
    "timestamp": timestamp,
    "score": score,
    "total_questions": len(filtered_questions),
    "category_filter": selected_category if selected_category else "All",
    "difficulty_filter": selected_difficulty if selected_difficulty else "All"
}

# Save score history
try:
    with open("score_history.json", "r") as history_file:
        history = json.load(history_file)
except FileNotFoundError:
    history = []

history.append(score_entry)

with open("score_history.json", "w") as history_file:
    json.dump(history, history_file, indent=2)

print("\n📜 Your Past Scores:")

for entry in history[-5:]:  # Show the last 5 games
    print(f"- {entry['timestamp']}: {entry['score']}/{entry['total_questions']} "
          f"(Category: {entry['category_filter']}, Difficulty: {entry['difficulty_filter']})")



