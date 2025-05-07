LISTA_COMPRA = []
option = ""

print("\n============= Programa Lista de la Compra ================\n")

while option != "Q":
    option= input("¿Que desea comprar? ([Q] para salir) >> ")
    if  option.upper() == "Q":
        continue

    option_safe = input(f"¿Seguro que quiere agregar {option}? [S/N] >> ").upper()
    if option_safe == "S":
        if option in LISTA_COMPRA:
            print(f"{option} ya esta en la lista!")
            continue
        LISTA_COMPRA.append(option)
        print(f"{option} agregado a la lista!\n")
    else:
        continue

print(f"\nLa Lista de la compra es: ")
print(LISTA_COMPRA)
