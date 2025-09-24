import random

questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the boiling point of water?": "100",
    "What is the smallest prime number?": "2",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the chemical symbol for gold?": "Au",
    "What year did the Titanic sink?": "1912",
    "What is the hardest natural substance on Earth?": "Diamond"
}


def get_question():
    question = random.choice(list(questions.keys()))
    print(f"Question: {question}")
    return question, questions[question]


def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()


def trivia_game():
    score = 0
    number_of_questions = 5
    for i in range(number_of_questions):
        question, answer = get_question()

        user_answer = input("Your answer: ")
        if check_answer(user_answer, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
    print(f"Your final score is: {score}/{number_of_questions}")


if __name__ == "__main__":
    trivia_game()
