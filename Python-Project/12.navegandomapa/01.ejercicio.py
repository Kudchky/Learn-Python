import os
import time
import readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OBJECTS = 10

my_position = [3, 1]
map_objects = []
for element in range(NUM_OBJECTS):
    x = random.randint(0, MAP_WIDTH - 1)
    y = random.randint(0, MAP_HEIGHT - 1)

    if [x, y] not in map_objects:
        map_objects.append([x, y])

while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for y in range(MAP_HEIGHT):
        print("|", end="")

        for x in range(MAP_WIDTH):
            # Player in the position
            if [x, y] == my_position:
                print(" @ ", end="")
                # If there is an object in the position of the player
                if [x, y] in map_objects:
                    map_objects.remove([x, y])
            # If only is an object
            elif [x, y] in map_objects:
                print(" # ", end="")
            # Empty space
            else:
                print("   ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #Ask the user where he wants to move
    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
        #if my_position[POS_Y] < 0:
        #    my_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
        #if my_position[POS_Y] > MAP_HEIGHT - 1:
        #    my_position[POS_Y] = 0
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
        #if my_position[POS_X] < 0:
        #    my_position[POS_X] = MAP_WIDTH - 1
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
        #if my_position[POS_X] > MAP_WIDTH - 1:
        #    my_position[POS_X] = 0
    elif direction == "q":
        break
    else:
        print("Enter a valid value: [W, S, A, D]")
        time.sleep(2)

    os.system("clear")

