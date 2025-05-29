print("\nBienvenido a App Tabla de Multiplicar\n"
      "--------------------------------------\n")
while True:
    try:
        numero_input = int(input("Ingrese un numero: ").strip())
        if numero_input <= 0:
            print("Error: Ingrese numeros enteros positivos mayor a 0, intente de nuevo\n")
            continue
        break
    except ValueError:
        print("Error: Ingrese valores numericos, intente de nuevo\n")

print(f"\nSe generó la tabla de multiplicar de {numero_input}")
print("---------------------------------------\n")

for numero in range(13):
    numero_multiplicado = numero_input * numero
    if numero_multiplicado % 2 == 0 and numero > 0:
        print(f"  {numero_input} x {numero} = {numero_multiplicado}")