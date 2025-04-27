# --- Questionary ---
DATA = [
    {
        "question": "¿What do you do, when do you see a cheese table?",
        "options": {
            "A": "I run away",
            "B": "I try one of the cheeses or even several",
            "C": "I cannot avoid devouring them all"
        },
        "points": {"A": 0, "B": 5, "C": 10}
    },
    {
        "question": "¿How do you like hamburgers?",
        "options": {
            "A": "Without cheese",
            "B": "Little cheese",
            "C": "With bread and cheese"
        },
        "points": {"A": 0, "B": 5, "C": 10}
    },
    {
        "question": "¿Are you lactose intolerant",
        "options": {
            "A": "Yes",
            "B": "Sometimes",
            "C": "No"
        },
        "points": {"A": 0, "B": 5, "C": 10}
    }
]

def message_welcome(message):
    print("\n" + message)
    print("_" * len(message) + "\n")

def assemble_question(question):
    print(question["question"])
    for key, value in question["options"].items():
        print(f"{key}: {value}")

    while True:
        answer = input("You answer (A, B, C):\n>>").upper()
        if answer in question["options"]:
            return answer
        else:
            print("You answer is invalidated. Please, enter A, B or C.")

def score_monitoring(answer, points):
    return points.get(answer, 0)

def show_score(total_score):
    print("\n ---Finally Result ---")
    if total_score >= 25:
        print("¡You really like cheese!")
    elif total_score >= 15:
        print("¡Does not dislike cheese!")
    else:
        print("¡Oh, you really hate the cheese!")

    print(f"You score final was: {total_score}")

def main():
    title = "Welcome the App ¿ Do you love cheese?"
    message_welcome(title)

    count_points = 0
    question_number = 1

    for data in DATA:
        print(f"\n--- Question {question_number} ---")
        user_answer = assemble_question(data)

        count_points += score_monitoring(user_answer, data["points"])
        question_number += 1

    show_score(count_points)

if __name__ == "__main__":
    main()

