import os
import time
import readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OBJECTS = 10

tail_length = 0
tail = []
my_position = [4, 2]
map_objects = []
obstacle_position = []

obstacle_definition = """\
# ######## ###     #
#  ####### ###   ###
##    #####    # ###
##### ##### ###    #
# ##          ## ###     
#######  ####    ###
  ######  ######   
  #######        ###
      ##############     
##  ##########   ###
###     ######     #
######  ######   ###
#######        #####
  #######    
#  ####### #########\
"""

obstacle_definition = [list(row.ljust(MAP_WIDTH)) for row in obstacle_definition.split("\n")]

for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        if obstacle_definition[y][x] == "#":
            obstacle_position.append([x, y])

def centered_message(message):
    screen_width = MAP_WIDTH * 3
    padding = (screen_width - len(message)) // 2
    print("\n" * (MAP_HEIGHT // 2))
    print(" " * padding + message)
    print("\n" * (MAP_HEIGHT // 2))

def add_object():
    while True:
        obj_x = random.randint(0, MAP_WIDTH - 1)
        obj_y = random.randint(0, MAP_HEIGHT - 1)
        if ([obj_x, obj_y] not in map_objects and
            [obj_x, obj_y] != my_position and
            [obj_x, obj_y] not in tail and
            [obj_x, obj_y] not in obstacle_position
        ):
            map_objects.append([obj_x, obj_y])
            break

def check_game_over():
    if my_position in tail or my_position in obstacle_position:
        time.sleep(1)
        os.system("clear")
        centered_message("💀 GAME OVER 💀")
        time.sleep(2)
        return True
    return False

while len(map_objects) < NUM_OBJECTS:
    x = random.randint(0, MAP_WIDTH - 1)
    y = random.randint(0, MAP_HEIGHT - 1)

    if ([x, y] not in map_objects and
        [x, y] != my_position and
        [x, y] not in obstacle_position
        ):
        map_objects.append([x, y])

while True:
    lose = False
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for y in range(MAP_HEIGHT):
        print("|", end="")

        for x in range(MAP_WIDTH):
            # Player in the position
            if [x, y] == my_position:
                print(" @ ", end="")
                # If there is an object in the position of the player.
                if [x, y] in map_objects:
                    map_objects.remove([x, y])
                    tail_length += 1
                    add_object()
            # If only is an object
            elif [x, y] in map_objects:
                print(" * ", end="")
            # If position is part of the obstacle
            elif [x, y] in obstacle_position:
                print("###", end="")
            # If the position is part of the tail.
            elif [x, y] in tail:
                print(" o ", end="")
            # Empty space
            else:
                print("   ", end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #Ask the user where he wants to move
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
        if len(tail) > tail_length:
            tail = tail[:tail_length]
        if check_game_over():
            break
    elif direction == "s":
        tail.insert(0, my_position.copy())
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
        if len(tail) > tail_length:
            tail = tail[:tail_length]
        if check_game_over():
            break
    elif direction == "a":
        tail.insert(0, my_position.copy())
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
        if len(tail) > tail_length:
            tail = tail[:tail_length]
        if check_game_over():
            break
    elif direction == "d":
        tail.insert(0, my_position.copy())
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
        if len(tail) > tail_length:
            tail = tail[:tail_length]
        if check_game_over():
            break
    elif direction == "q":
        print("You left the game...!")
        break
    else:
        print("Enter a valid value: [W, S, A, D]")
        time.sleep(1)

    os.system("clear")

