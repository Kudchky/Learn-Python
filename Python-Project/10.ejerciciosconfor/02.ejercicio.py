texto_usuario = "Hola me llamo Nate, ¿tú cómo te llamas?"
contador_mayusculas = 0

for character in texto_usuario:
    if character.isupper():
        contador_mayusculas += 1

print(f"""
El texto introducido por el usuario:
'{texto_usuario}'

Tiene: {contador_mayusculas} mayusculas
""")
