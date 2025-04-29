# Smart Quiz App (Python CLI)

A beginner-friendly Python quiz app that runs in the terminal.  
You can filter questions by category and difficulty, answer flexibly (case-insensitive, punctuation-tolerant), race against a timer, and track your score history over time!

---

## Features

- Load questions from a structured JSON file
- Accepts multiple correct answers per question
- Case-insensitive + punctuation-tolerant input
- Filter questions by **category** and **difficulty**
- Randomized question order
- Optional timed questions (⏰)
- Colored terminal output with `colorama`
- Score history saved to `score_history.json` after every game

---

## How to Run

1. Make sure you have **Python 3** installed  
2. Clone this repo or download the project folder  
3. Install the required packages:
   ```bash
   pip install -r requirements.txt

Run the app: 
    python main.py

Example Question Format (questions.json)

    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "paris"],
        "category": "Geography",
        "difficulty": "Easy"
    }

You can add as many questions as you like — just follow this format inside the JSON file.

Score History
    After every quiz, a new entry is saved in score_history.json, including:

        Your score
        Number of questions
        Selected filters (category and difficulty)
        Timestamp (date and time)
    
    Example: 

    {
        "timestamp": "2025-04-29 16:00:00",
        "score": 3,
        "total_questions": 4,
        "category_filter": "Math",
        "difficulty_filter": "Easy"
    }

Built With
    Python 3
    colorama — for colorful terminal messages
    inputimeout — to allow timed user input
    Git & GitHub — for version control and publishing

Built with love by Mohamed Anouar Zaki
Feel free to fork, improve, or share!

This project is open-source and free to use. MIT License by default.



