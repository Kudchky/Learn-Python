LISTA_NUMEROS = []

while True:
    try:
        numero_input = int(input("Ingrese un numero a la lista: "))
        LISTA_NUMEROS.append(numero_input)

        while True:
            option = input("Desea ingresar mas números? [S/N]: ").strip().upper()
            if option == "S":
                break
            elif option == "N":
                break
            else:
                print("Ingrese solo [S/N], pruebe de nuevo")

        if option == "N":
            break
    except ValueError:
        print("Error: Ingrese un valor numérico, inténtelo de nuevo")

if LISTA_NUMEROS:
    print(f"\nLa lista de números es: {LISTA_NUMEROS}")

    numero_mayor = 0
    numero_menor = 0
    for element in LISTA_NUMEROS:
        if numero_mayor < element:
            numero_mayor = element

        if numero_menor > element:
            numero_menor = element

    print(f"""
    N° menor: {numero_menor} 
    N° mayor: {numero_mayor}
    """)
else:
    print("La lista esta vacía, no se ingresaron números")



#print(min(LISTA_NUMEROS))
#print(max(LISTA_NUMEROS))