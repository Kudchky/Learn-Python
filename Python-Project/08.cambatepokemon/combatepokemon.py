import random

ataques_pokemon = {
    "Pikachu": {
        "1": {"ataque": "Impacttrueno", "dano": 15, "tipo": "Electrico"},
        "2": {"ataque": "Rayo", "dano": 25, "tipo": "Electrico"},
        "3": {"ataque": "Ataque Rapido", "dano": 10, "tipo": "Normal"},
        "4": {"ataque": "Placaje", "dano": 8, "tipo": "Normal"}
    },
    "Squirtle": {
        "1": {"ataque": "Pistola Agua", "dano": 12, "tipo": "Agua"},
        "2": {"ataque": "Hidrobomba", "dano": 30, "tipo": "Agua"},
        "3": {"ataque": "Placaje", "dano": 8, "tipo": "Normal"},
        "4": {"ataque": "Burbuja", "dano": 10, "tipo": "Agua"}
    }
}

vida_inicial_picachu = 80
vida_inicial_squirtle = 90

vida_picachu = vida_inicial_picachu
vida_squirtle = vida_inicial_squirtle

turno = random.randint(0,1)

def barra_vida(vida_pokemon, pokemon):
    if pokemon == "Picachu":
        result = round(vida_pokemon * 10 / vida_inicial_picachu, 2)
        cadena = f'{"▓" * int(result)}{"░" * (10 - int(result))}'
        print(f"{pokemon}    [{cadena}] {result * 10}%")
    else:
        result = round(vida_pokemon * 10 / vida_inicial_squirtle, 2)
        cadena = f'{"▓" * int(result)}{"░" * (10 - int(result))}'
        print(f"{pokemon}   [{cadena}] {result * 10}%\n")


print("\nEmpiza la Batalla Pokemon entre PICACHU y SQUIRTLE\n"
      "===================================================\n")
barra_vida(vida_picachu, "Picachu")
barra_vida(vida_squirtle, "Squirtle")

while vida_picachu > 0 and vida_squirtle > 0:
    if turno == 0:
        print("Es tu turno de atacar, Vamos PIKACHU...!\n")
        ataque = ataques_pokemon["Pikachu"][str(random.randint(1, 4))]
        print(f"¡Genial, Picachu ataca con {ataque['ataque']}, son {ataque['dano']} de dano\n")
        vida_squirtle -= ataque["dano"]
        if vida_squirtle < 0:
            vida_squirtle = 0

        barra_vida(vida_picachu, "Picachu")
        barra_vida(vida_squirtle, "Squirtle")
        turno = 1
    else:
        print("Es tu turno de atacar, Vamos SQUIRTLE... !\n")
        option = input("""
        1) Pistola Agua.
        2) Hidrobomba.
        3) Placaje.
        4) Burbuja.
        
        ¿Cual ataque eliges? >> 
        """)
        ataque = ataques_pokemon["Squirtle"][option]
        print(f"¡Genial, Squirtle ataca con {ataque['ataque']}, son {ataque['dano']} de dano\n")
        vida_picachu -= ataque["dano"]
        if vida_picachu < 0:
            vida_picachu = 0
        barra_vida(vida_picachu, "Picachu")
        barra_vida(vida_squirtle, "Squirtle")
        turno = 0

if vida_squirtle > vida_picachu:
    print("El ganador es SQUIRTLE...")
else:
    print("El ganador ha sido PICACHU...")
