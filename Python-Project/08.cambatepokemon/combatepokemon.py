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

vida_picachu = 80
vida_squirtle = 90

turno = random.randint(0,1)

def barra_vida(vida_pokemon, pokemon):
    if pokemon == "Picachu":
        result = int(vida_pokemon * 10 / 80)
        return ["#" * result + " " * (10 - result), result]
    else:
        result = int(vida_pokemon * 10 / 90)
        return ["#" * result + " " * (10 - result), result]


print("\nEmpiza la Batalla Pokemon entre PICACHU y SQUIRTLE\n"
      "===================================================\n")
while vida_picachu > 0 and vida_squirtle > 0:
    if turno == 0:
        print("Es tu turno de atacar, Vamos PIKACHU...!\n")
        ataque = ataques_pokemon["Pikachu"][str(random.randint(1, 4))]
        print(f"¡Genial, Picachu ataca con {ataque['ataque']}, son {ataque['dano']} de dano\n")
        vida_squirtle -= ataque["dano"]
        [cadena_picachu, result_picachu] = barra_vida(vida_picachu, "Picachu")
        [cadena_squirtle, result_squirtle] = barra_vida(vida_squirtle, "Squirtle")

        print(f"La vida de Picachu es: {vida_picachu} [{cadena_picachu}] {result_picachu * 10}%\n"
              f"la vida de Squirtle es: {vida_squirtle} [{cadena_squirtle}] {result_squirtle * 10}%\n")
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
        print(f"la vida de Squirtle es: {vida_squirtle} [{barra_vida(vida_squirtle, 'Squirtle')}]\n"
              f"La vida de Picachu es: {vida_picachu} [{barra_vida(vida_picachu, 'Picachu')}]")
        turno = 0

if vida_squirtle > vida_picachu:
    print("El ganador es SQUIRTLE...")
else:
    print("El ganador ha sido PICACHU...")
