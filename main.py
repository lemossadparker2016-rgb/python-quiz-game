QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": {
            "A": "London",
            "B": "Paris",
            "C": "Madrid",
            "D": "Rome"
        },
        "answer": "B"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": {
            "A": "HTML",
            "B": "Python",
            "C": "C++",
            "D": "Java"
        },
        "answer": "A"
    },
    {
        "question": "How many days are there in a week?",
        "options": {
            "A": "Five",
            "B": "Six",
            "C": "Seven",
            "D": "Eight"
        },
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Venus",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Saturn"
        },
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": {
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Utility",
            "D": "Control Processing User"
        },
        "answer": "A"
    }
]


def play_quiz():
    score = 0

    print("\n" + "=" * 40)
    print("          PYTHON QUIZ GAME")
    print("=" * 40)

    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for letter, option in question["options"].items():
            print(f"  {letter}. {option}")

        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()

            if answer in question["options"]:
                break

            print("Invalid choice. Please enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            correct_answer = question["answer"]
            correct_option = question["options"][correct_answer]
            print(f"Incorrect! The correct answer is {correct_answer}. {correct_option}")

    percentage = (score / len(QUESTIONS)) * 100

    print("\n" + "=" * 40)
    print("             QUIZ RESULTS")
    print("=" * 40)
    print(f"Your score: {score}/{len(QUESTIONS)}")
    print(f"Your percentage: {percentage:.1f}%")

    if score == len(QUESTIONS):
        print("Excellent! Perfect score!")
    elif score >= 3:
        print("Good job! Keep practicing!")
    else:
        print("Keep learning! You can do better!")

    print("=" * 40)


def main():
    while True:
        play_quiz()

        while True:
            replay = input("\nWould you like to play again? (Y/N): ").strip().upper()

            if replay in ("Y", "N"):
                break

            print("Invalid choice. Please enter Y or N.")

        if replay == "N":
            print("\nThank you for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
