import os
import time
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]
map_objects = [[2, 3], [5, 4], [3, 4], [10, 6], [18, 12]]

while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            drawn = False
            #Drawn the player
            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                print(" @ ", end="")
                drawn = True
            #Drawn objects if the player is not
            if drawn:
                for obj in map_objects:
                    if (coordinate_x == obj[POS_X] and coordinate_y == obj[POS_Y]) and (coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]):
                        map_objects.remove(obj)
                        break
            elif not drawn:
                for obj in map_objects:
                    if coordinate_x == obj[POS_X] and coordinate_y == obj[POS_Y]:
                        print(" # ", end="")
                        drawn = True
                        break

            #if you did not draw the player or the object, empty space.
            if not drawn:
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

