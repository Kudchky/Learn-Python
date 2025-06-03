import os
import time
import readchar
import random

vida_pokemons = {
    "Pikachu": 100,
    "Squirtle": 110,
    "Charmander": 95,
    "Bulbasaur": 105,
    "Eevee": 100,
    "Jigglypuff": 120,
    "Psyduck": 98
}


ataques_pokemon = {
    "Pikachu": {
        1: {"ataque": "Impact Trueno", "dano": 15, "tipo": "Electrico"},
        2: {"ataque": "Rayo", "dano": 25, "tipo": "Electrico"},
        3: {"ataque": "Ataque Rapido", "dano": 10, "tipo": "Normal"},
        4: {"ataque": "Placaje", "dano": 8, "tipo": "Normal"},
        5: {"ataque": "No ataques", "dano": 0},
    },
    "Squirtle": {
        1: {"ataque": "Pistola de Agua", "dano": 12, "tipo": "Agua"},
        2: {"ataque": "Hidrobomba", "dano": 30, "tipo": "Agua"},
        3: {"ataque": "Placaje", "dano": 8, "tipo": "Normal"},
        4: {"ataque": "Burbuja", "dano": 10, "tipo": "Agua"},
        5: {"ataque": "No atacar", "dano": 0}
    },
    "Charmander": {
        1: {"ataque": "Ascuas", "dano": 14, "tipo": "Fuego"},
        2: {"ataque": "Lanzallamas", "dano": 28, "tipo": "Fuego"},
        3: {"ataque": "Arañazo", "dano": 10, "tipo": "Normal"},
        4: {"ataque": "Giro Fuego", "dano": 18, "tipo": "Fuego"},
        5: {"ataque": "No atacar", "dano": 0}
    },
    "Bulbasaur": {
        1: {"ataque": "Látigo Cepa", "dano": 12, "tipo": "Planta"},
        2: {"ataque": "Hoja Afilada", "dano": 22, "tipo": "Planta"},
        3: {"ataque": "Placaje", "dano": 8, "tipo": "Normal"},
        4: {"ataque": "Drenadoras", "dano": 15, "tipo": "Planta"},
        5: {"ataque": "No atacar", "dano": 0}
    },
    "Eevee": {
        1: {"ataque": "Ataque Rápido", "dano": 10, "tipo": "Normal"},
        2: {"ataque": "Mordisco", "dano": 18, "tipo": "Siniestro"},
        3: {"ataque": "Doble Golpe", "dano": 16, "tipo": "Normal"},
        4: {"ataque": "Bola Sombra", "dano": 20, "tipo": "Fantasma"},
        5: {"ataque": "No atacar", "dano": 0}
    },
    "Jigglypuff": {
        1: {"ataque": "Canto", "dano": 0, "tipo": "Normal"},
        2: {"ataque": "Rizo Defensa", "dano": 5, "tipo": "Normal"},
        3: {"ataque": "Desenrollar", "dano": 15, "tipo": "Roca"},
        4: {"ataque": "Golpe Cuerpo", "dano": 20, "tipo": "Normal"},
        5: {"ataque": "No atacar", "dano": 0}
    },
    "Psyduck": {
        1: {"ataque": "Confusión", "dano": 18, "tipo": "Psíquico"},
        2: {"ataque": "Pistola Agua", "dano": 12, "tipo": "Agua"},
        3: {"ataque": "Cabezazo", "dano": 15, "tipo": "Normal"},
        4: {"ataque": "Psicorrayo", "dano": 25, "tipo": "Psíquico"},
        5: {"ataque": "No atacar", "dano": 0}
    }

}

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
# Variables Battle Pokemon


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def init_battle():
    pokemon_maquina = random.choice(list(vida_pokemons.keys()))
    pokemon_user = "Pikachu"

    vida_inicial_maquina = vida_pokemons[pokemon_maquina]
    vida_inicial_usuario = vida_pokemons[pokemon_user]

    vida_maquina = vida_inicial_maquina
    vida_user = vida_inicial_usuario

    turno = random.randint(0,1)

    def barra_vida(vida_pokemon, vida_total, pokemon):
        result = round(vida_pokemon * 10 / vida_total, 2)
        cadena = f'{"▓" * int(result)}{"░" * (10 - int(result))}'
        print(f"{pokemon:<12} [{cadena}] {result * 10:5.1f}%")

    print("\nPokemon battle begins, good luck...........\n"
          "=============================================\n")
    barra_vida(vida_maquina, vida_inicial_maquina, pokemon_maquina)
    barra_vida(vida_user, vida_inicial_usuario, pokemon_user)

    while vida_maquina > 0 and vida_user > 0:
        if turno == 0:
            print(f"\nIt's your turn to attack, let's go {pokemon_maquina} CPU...!\n")
            input("Press Enter to continue...!")
            ataque = ataques_pokemon[pokemon_maquina][random.randint(1, 5)]
            print(f"¡Great {pokemon_maquina} CPU, {ataque['ataque']} are: {ataque['dano']} damage "
                  f"points ")
            vida_user -= ataque["dano"]

            if vida_user < 0:
                vida_user = 0

            barra_vida(vida_maquina, vida_inicial_maquina, pokemon_maquina)
            barra_vida(vida_user, vida_inicial_usuario, pokemon_user)
            input("\nPress Enter to continue...!")
            limpiar_pantalla()
            turno = 1
        else:
            print(f"\nIt's your turn to attack, let's go {pokemon_user}... !\n")
            input("Press Enter to continue...!")
            option = 0
            while option < 1 or option > 5:
                try:
                    option = int(input(f"""
                    1) {ataques_pokemon[pokemon_user][1]['ataque']}
                    2) {ataques_pokemon[pokemon_user][2]['ataque']}
                    3) {ataques_pokemon[pokemon_user][3]['ataque']}
                    4) {ataques_pokemon[pokemon_user][4]['ataque']}
                    5) {ataques_pokemon[pokemon_user][5]['ataque']}
                    
                    Which attack do you choose? >> """))
                except ValueError:
                    print("Only the options from 1 to 5 are valid.\n")
                    option = 0

            ataque = ataques_pokemon[pokemon_user][option]
            print(f"\n¡Great {pokemon_user}, {ataque['ataque']} are: {ataque['dano']} damage points")
            vida_maquina -= ataque["dano"]
            if vida_maquina < 0:
                vida_maquina = 0
            barra_vida(vida_maquina, vida_inicial_maquina, pokemon_maquina)
            barra_vida(vida_user, vida_inicial_usuario, pokemon_user)
            input("\nPress Enter to continue...!")
            limpiar_pantalla()
            turno = 0

    if vida_user > vida_maquina:
        print(f"The Winner is {pokemon_user}...")
        print("You Win this battle")
        return True
    else:
        print(f"The winner has been {pokemon_maquina}...\n")
        print("You Lost The Game...")
        return False
#End Battle Pokemon

WIDTH = 20
HEIGHT = 15
world_pokemon_split = [list(line.ljust(WIDTH)) for line in world_pokemon.split("\n")]
user_pokemon = [1, 14]
gyms = []
master = []
obstacle = []
game_over = False
battle_pokemon = False
count_battle = 0
reiniciar = False

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
    print("\nWelcome Game Pokemon Snake")
    print("--------------------------\n")
    print("Warning:Do not approach the gym walls, you will lose the battle.")
    # Print Map
    while flag:
        print("+" + "-" * 3 * WIDTH + "+")
        for y in range(HEIGHT):
            print("|", end="")
            for x in range(WIDTH):
                if [x, y] == user_pokemon:
                    if [x, y] in gyms:
                        print(" x ", end="")
                        game_over = True
                    elif [x, y] in master:
                        count_battle += 1
                        battle_pokemon = True
                        print(" ☺ ", end="")
                    else:
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
    if not master:
        time.sleep(2)
        print("\nYou earned Pokemon Snake, congratulations you are the best of all")
        break

    if game_over:
        print("\nYou crashed with the gym wall, they are a trap")
        print(" GAME OVER ")
        break

    if battle_pokemon:
        time.sleep(1)
        os.system("clear")
        print("\nWelcome Battle Pokemon")
        print("-----------------------")
        if init_battle():
            master.remove(user_pokemon)
            reiniciar = True
        else:
            print(" GAME OVER ")
            break
        time.sleep(2)
        battle_pokemon = False

    if reiniciar:
        reiniciar = False
        continue
    # Move PokemonSnake
    print("Press a key (w, s, a, d) or q to exit...!")

    move = readchar.readchar().lower()

    match move:
        case "w":
            user_pokemon[1] -= 1
            user_pokemon[1] %= HEIGHT
            if user_pokemon in obstacle:
                user_pokemon[1] += 1

        case "s":
            user_pokemon[1] += 1
            user_pokemon[1] %= HEIGHT
            if user_pokemon in obstacle:
                user_pokemon[1] -= 1
        case "a":
            user_pokemon[0] -= 1
            user_pokemon[0] %= WIDTH
            if user_pokemon in obstacle:
                user_pokemon[0] += 1
        case "d":
            user_pokemon[0] += 1
            user_pokemon[0] %= WIDTH
            if user_pokemon in obstacle:
                user_pokemon[0] -= 1
        case "q":
            break
        case _:
            print("Key incorrect, enter a key again...")
            time.sleep(0.8)
    # End Move PokemonSnake
    os.system("clear")