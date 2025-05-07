import random
import os

ataques_pokemon = {
    "Pikachu": {
        1: {"ataque": "Impact Trueno", "dano": 15, "tipo": "Electrico"},
        2: {"ataque": "Rayo", "dano": 25, "tipo": "Electrico"},
        3: {"ataque": "Ataque Rapido", "dano": 10, "tipo": "Normal"},
        4: {"ataque": "Placaje", "dano": 8, "tipo": "Normal"},
        5: {"ataque": "No ataques", "dano": 0}
    },
    "Squirtle": {
        1: {"ataque": "Pistola de Agua", "dano": 12, "tipo": "Agua"},
        2: {"ataque": "Hidrobomba", "dano": 30, "tipo": "Agua"},
        3: {"ataque": "Placaje", "dano": 8, "tipo": "Normal"},
        4: {"ataque": "Burbuja", "dano": 10, "tipo": "Agua"},
        5: {"ataque": "No atacar", "dano": 0}
    }
}

vida_inicial_picachu = 80
vida_inicial_squirtle = 90

vida_picachu = vida_inicial_picachu
vida_squirtle = vida_inicial_squirtle

turno = random.randint(0,1)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Limpieza de pantalla...\n")

def barra_vida(vida_pokemon, vida_total, pokemon):
        result = round(vida_pokemon * 10 / vida_total, 2)
        cadena = f'{"▓" * int(result)}{"░" * (10 - int(result))}'
        print(f"{pokemon}    [{cadena}] {round(result * 10, 2)}%")

print("\nEmpiza la Batalla Pokemon entre PICACHU y SQUIRTLE\n"
      "===================================================\n")
barra_vida(vida_picachu, vida_inicial_picachu,"Picachu")
barra_vida(vida_squirtle, vida_inicial_squirtle,"Squrtle")

while vida_picachu > 0 and vida_squirtle > 0:
    if turno == 0:
        print("\nEs tu turno de atacar, Vamos PIKACHU...!\n")
        input("Presione Enter para continuar...!")
        ataque = ataques_pokemon["Pikachu"][random.randint(1, 5)]
        print(f"¡Genial, Picachu {ataque['ataque']}, son {ataque['dano']} puntos de dano")
        vida_squirtle -= ataque["dano"]

        if vida_squirtle < 0:
            vida_squirtle = 0

        barra_vida(vida_picachu, vida_inicial_picachu,"Picachu")
        barra_vida(vida_squirtle, vida_inicial_squirtle,"Squrtle")
        input("\nPresione Enter para conitnuar...!")
        limpiar_pantalla()
        turno = 1
    else:
        print("\nEs tu turno de atacar, Vamos SQUIRTLE... !\n")
        input("Presione Enter para continuar...!")
        option = 0
        while option < 1 or option > 5:
            try:
                option = int(input("""
                1) Pistola Agua.
                2) Hidrobomba.
                3) Placaje.
                4) Burbuja.
                5) No Atacar.
                
                ¿Cual ataque eliges? >>"""))
            except ValueError:
                print("Solo son validas las opciones del 1 al 5.\n")
                option = 0

        ataque = ataques_pokemon["Squirtle"][option]
        print(f"\n¡Genial, Squirtle {ataque['ataque']}, son {ataque['dano']} puntos de dano")
        vida_picachu -= ataque["dano"]
        if vida_picachu < 0:
            vida_picachu = 0
        barra_vida(vida_picachu, vida_inicial_picachu,"Picachu")
        barra_vida(vida_squirtle, vida_inicial_squirtle,"Squrtle")
        input("\nPresione Enter para continuar...!")
        limpiar_pantalla()
        turno = 0

if vida_squirtle > vida_picachu:
    print("El ganador es SQUIRTLE...\n")
else:
    print("El ganador ha sido PICACHU...\n")
