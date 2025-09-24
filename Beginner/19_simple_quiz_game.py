def run_quiz(questions):
    """
    Runs a multiple-choice quiz, keeps score, and displays the final result.
    """
    # 2. Initialize score
    score = 0

    # 3. Loop through the questions
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # 4. Prompt for answer and check if correct
        user_answer = input("Your answer (A, B, C, or D): ").upper()
        
        if user_answer == q['answer']:
            print("Correct!")
            # 5. Update score
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    # 6. Display final score
    print(f"\nQuiz finished! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    # 1. Create a list of questions
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
            "answer": "B"
        }
    ]

    print("--- Simple Quiz Game ---")
    run_quiz(quiz_questions)