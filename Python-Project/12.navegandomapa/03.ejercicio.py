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
TRACE_SNAKE = []
TAIL_SNAKE = []
count_food = 0

#Funtions----
def add_food():
    while len(LIST_FOOD) < MAX_FOOD:
        food_x = random.randint(0, WIDTH - 1)
        food_y = random.randint(0, HEIGHT - 1)
        if ([food_x, food_y] != my_position and
            [food_x, food_y] not in LIST_FOOD and
            [food_x, food_y] not in TAIL_SNAKE
        ):
            LIST_FOOD.append([food_x, food_y])

def move_snake(position):
    global TAIL_SNAKE
    print("Press a key (w, s, a, d) or q to exit...!")
    key = readchar.readchar().upper()
    match key:
        case "W":
            # Define trace snake
            TRACE_SNAKE.insert(0, position)
            # Define tail snake
            if count_food > 0:
                TAIL_SNAKE = TRACE_SNAKE[: count_food]
            # Define position new
            position = [position[0], position[1] - 1]
            # Define that snake appears to the other side
            if position[1] == -1:
                position = [position[0], HEIGHT - 1]
        case "S":
            TRACE_SNAKE.insert(0, position)
            if count_food > 0:
                TAIL_SNAKE = TRACE_SNAKE[: count_food]
            position = [position[0], position[1] + 1]
            if position[1] == HEIGHT:
                position = [position[0], 0]
        case "A":
            TRACE_SNAKE.insert(0, position)
            if count_food > 0:
                TAIL_SNAKE = TRACE_SNAKE[: count_food]
            position = [position[0] - 1, position[1]]
            if position[0] == -1:
                position = [WIDTH - 1, position[1]]
        case "D":
            TRACE_SNAKE.insert(0, position)
            if count_food > 0:
                TAIL_SNAKE = TRACE_SNAKE[: count_food]
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
                        count_food += 1
                        add_food()
                elif [x, y] in TAIL_SNAKE:
                    print(" o ", end="")
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

