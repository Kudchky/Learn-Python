fahrenheit = int(input("Digite la temperatura en Fahrenheit: "))

def conversor(f):
    celsius = (f - 32) * 5 / 9
    return celsius

print("La temperatura en Celsius es: ", conversor(fahrenheit))