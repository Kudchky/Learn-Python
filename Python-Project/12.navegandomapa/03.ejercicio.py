# Define constants
import os
import random
import time
import readchar

my_position = [5, 3]
WIDTH = 20
HEIGHT = 15
MAX_FOOD = 10
LIST_FOOD = []

#Funtions----
def add_food():
    while len(LIST_FOOD) < MAX_FOOD:
        food_x = random.randint(0, WIDTH - 1)
        food_y = random.randint(0, HEIGHT - 1)
        if [food_x, food_y] != my_position:
            LIST_FOOD.append([food_x, food_y])

def move_snake(position):
    print("Press a key (w, s, a, d) or q to exit...!")
    key = readchar.readchar().upper()
    match key:
        case "W":
            position = [position[0], position[1] - 1]
            if position[1] == -1:
                position = [position[0], HEIGHT - 1]
        case "S":
            position = [position[0], position[1] + 1]
            if position[1] == HEIGHT:
                position = [position[0], 0]
        case "A":
            position = [position[0] - 1, position[1]]
            if position[0] == -1:
                position = [WIDTH - 1, position[1]]
        case "D":
            position = [position[0] + 1, position[1]]
            if position[0] == WIDTH:
                position = [0, position[1]]
        case "Q":
            return "exit"
        case _:
            print("Key incorrect...!")
            time.sleep(0.9)

    return position
#Fin----

add_food()

while True:
    print("\n\n                      Welcome To Snake Game")
    print("+" + "-" * WIDTH * 3 + "+")
    flag = True
    while flag:
        for y in range(HEIGHT):
            print("|", end="")
            for x in range(WIDTH):
                if [x, y] == my_position:
                    print(" @ ", end="")
                    if [x, y] in LIST_FOOD:
                        LIST_FOOD.remove([x, y])
                elif [x, y] in LIST_FOOD:
                    print(" ■ ", end="")
                else:
                    print(" . ", end="")
            print("|")

        flag = False

    print("+" + "-" * WIDTH * 3 + "+")

    #Press a Key
    my_position = move_snake(my_position)
    if my_position == "exit":
        break

    os.system("clear")

