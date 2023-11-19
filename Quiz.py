import random

# Quiz Questions
quiz_questions = [
    {
        "question": "What is the capital of Canada?",
        "choices": ["Toronto", "Montreal", "Ottawa", "Quebec"],
        "answer": "Ottawa"
    },
    {
        "question": "Which Indian City is known as City of Pearls?",
        "choices": ["Surat", "Hyderabad", "Pune", "Bengaluru"],
        "answer": "Hyderabad"
    },
    {
        "question": "Which of these is a month not having 5 sundays in 2023?",
        "choices": ["April", "July", "August", "October"],
        "answer": "August"
    }
    # Add more questions here...
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Choose the correct answer!")

def present_quiz_question(question_obj):
    print("\nQuestion:", question_obj["question"])
    for idx, choice in enumerate(question_obj["choices"], start=1):
        print(f"{idx}. {choice}")
    user_answer = input("Your answer (enter the number or text): ")
    return user_answer

def evaluate_answer(question, user_answer):
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct answer is: {question['answer']}")
        return 0

def calculate_final_score(score, total_questions):
    return f"You scored {score} out of {total_questions} questions correctly."

def play_quiz():
    display_welcome_message()
    random.shuffle(quiz_questions)
    total_questions = len(quiz_questions)
    score = 0

    for question in quiz_questions:
        user_answer = present_quiz_question(question)
        score += evaluate_answer(question, user_answer)

    final_result = calculate_final_score(score, total_questions)
    print("\n" + final_result)

if __name__ == "__main__":
    play_again = True
    while play_again:
        play_quiz()
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == "yes"
    print("Thanks for playing!")