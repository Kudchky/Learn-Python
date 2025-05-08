LISTA_COMPRA = []
option = ""

print("\n============= Programa Lista de la Compra ================\n")

while True:
    option= input("¿Que desea comprar? ([Q] para salir) >> ").strip().upper()
    if  option.upper() == "Q":
        break

    option_safe = input(f"¿Seguro que quiere agregar {option}? [S/N] >> ").strip().upper()
    if option_safe == "S":
        if option in LISTA_COMPRA:
            print(f"{option} ya esta en la lista!\n")
            continue
        LISTA_COMPRA.append(option)
        print(f"{option} agregado a la lista!\n")
    else:
        print("No se agrego nada a la lista.\n")
        continue

print(f"\nLa Lista de la compra es: \n" + ", ".join(LISTA_COMPRA))
