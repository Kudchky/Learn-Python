import os
import time
import readchar

world_pokemon = """\
%    %   %      M %% 
%% %   %   %%%%%%%%%
    %%% #%#   
     %%%%%%    ##
 ##  % M  %    ##     
###  %%%% % ##   ###
     
      ###
      #          ###
##    # %%% %   ###
        % M %   
        %%%%% %%%% %
###           %%%% %
##  ###       % M  % 
              %%%%%%\
"""

WIDTH = 20
HEIGHT = 15
world_pokemon_split = [list(line.ljust(WIDTH)) for line in world_pokemon.split("\n")]
user_pokemon = [1, 14]
gyms = []
master = []
obstacle = []
game_over = False

for row in range(HEIGHT):
    for column in range(WIDTH):
        if world_pokemon_split[row][column] == "%":
            gyms.append([column, row])
        elif world_pokemon_split[row][column] == "M":
            master.append([column, row])
        elif world_pokemon_split[row][column] == "#":
            obstacle.append([column, row])



while not game_over:
    flag = True
    print("      Welcome Game Pokemon Snake  ")
    print("Warning:Do not approach the gym walls, you will lose the battle.")
    # Print Map
    while flag:
        print("+" + "-" * 3 * WIDTH + "+")
        for y in range(HEIGHT):
            print("|", end="")
            for x in range(WIDTH):
                if [x, y] == user_pokemon:
                    print(" ☺ ", end="")
                elif [x, y] in gyms:
                    print("███", end="")
                elif [x, y] in obstacle:
                    print("▒▒▒", end="")
                elif [x, y] in master:
                    print(" ☠ ", end="")
                else:
                    print(" . ", end="")
            print("|")
        print("+" + "-" * 3 * WIDTH + "+")
        flag = False
    # End Print Map

    # Move PokemonSnake
    print("Press a key (w, s, a, d) or q to exit...!")
    move = readchar.readchar().lower()

    match move:
        case "w":
            user_pokemon[1] -= 1
            user_pokemon[1] %= HEIGHT
        case "s":
            user_pokemon[1] += 1
            user_pokemon[1] %= HEIGHT
        case "a":
            user_pokemon[0] -= 1
            user_pokemon[0] %= WIDTH
        case "d":
            user_pokemon[0] += 1
            user_pokemon[0] %= WIDTH
        case "q":
            break
        case _:
            print("Key incorrect, enter a key again...")
            time.sleep(0.8)
    # End Move PokemonSnake
    os.system("clear")