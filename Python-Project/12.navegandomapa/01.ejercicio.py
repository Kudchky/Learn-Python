import os
import time
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #Ask the user where he wants to move
    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
        if my_position[POS_Y] < 0:
            my_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "s":
        my_position[POS_Y] += 1
        if my_position[POS_Y] > MAP_HEIGHT - 1:
            my_position[POS_Y] = 0
    elif direction == "a":
        my_position[POS_X] -= 1
        if my_position[POS_X] < 0:
            my_position[POS_X] = MAP_WIDTH - 1
    elif direction == "d":
        my_position[POS_X] += 1
        if my_position[POS_X] > MAP_WIDTH - 1:
            my_position[POS_X] = 0
    elif direction == "q":
        break
    else:
        print("Enter a valid value: [W, S, A, D]")
        time.sleep(2);

    os.system("clear")

