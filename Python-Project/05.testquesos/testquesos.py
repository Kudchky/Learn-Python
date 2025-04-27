title = "Welcome to the Cheese App, you like the cheese?"
print("\n" + title + "\n" + "_"*len(title) + "\n")

points = 0

def user_choice (answer):
    global points

    if answer == "A":
        points += 0
    elif answer == "B":
        points += 5
    elif answer =="C":
        points += 10
    else:
        print("Enter a value between A, B or C")
        exit()

def score():
    if points >= 25:
        print("!You really like cheese")
    elif 15 <= points:
        print("You don't like cheese so much!")
    else:
        print("¡Oh, you hate cheese....!")

    print(f"¡You score was {points}")


answer_user = input("Question 1.- ¿What do you do, when do you see a cheese table?\n"
                    "A: I run away\n"
                    "B: I try one of the cheeses or even several\n"
                    "C: I cannot avoid devouring them all\n")

user_choice(answer_user)


answer_user = input("Question 2.- ¿How do you like hamburgers?\n"
                    "A: Without cheese\n"
                    "B: Little cheese\n"
                    "C: With bread and cheese\n")

user_choice(answer_user)

answer_user = input("Question 3.- ¿Are you lactose intolerant\n"
                    "A: Yes\n"
                    "B: Sometimes\n"
                    "C: No\n")

user_choice(answer_user)

score()


