import random

print("Bienvenido al juego de adivinar el numero")
print("=========================================")

numero_aleatorio = random.randint(1, 10)
entrada_usuario = input("Ingrese un numero entre 1 y 10: ")

try :
    numero_ingresado = int(entrada_usuario)

    if 1 <= numero_ingresado <= 10 :
        if numero_ingresado == numero_aleatorio :
            print(f"Enhorabuena acertaste, {numero_aleatorio} era el numero")
        else:
            print(f"Mejor suerte para la proxima, el numero era {numero_aleatorio}")
    else :
        print(f"Ingrese un numero entre 1 y 10")
        print(f"El numero secreto era {numero_aleatorio}")
        print("Fin del juego")

except ValueError :
    print("Ingrese un numero entero")
    print(f"El numero secreto era {numero_aleatorio}")
    print("Fin del juego")
