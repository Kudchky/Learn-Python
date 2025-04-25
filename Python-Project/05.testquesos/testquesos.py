title = "Welcome to the Cheese App, you like the cheese?"
print("\n" + title + "\n" + "_"*len(title) + "\n")

points = 0

answer_user = input("Question 1.- ¿What do you do, when do you see a cheese table?\n"
                    "A: I run away\n"
                    "B: I try one of the cheeses or even several\n"
                    "C: I cannot avoid devouring them all\n")

if answer_user == "A":
    points += 0
elif answer_user == "B":
    points += 5
elif answer_user =="C"
    points += 10
else:
    print("Enter a value between A, B or C")

answer_user = input("Question 2.- ¿How do you like hamburgers?\n"
                    "A: With cheese\n"
                    "B: Without cheese\n"
                    "C: With bread and cheese\n")

answer_user = input("Question 3.- ¿Are you lactose intolerant\n"
                    "A: Yes\n"
                    "B: Sometimes\n"
                    "C: No\n")

print(points)
