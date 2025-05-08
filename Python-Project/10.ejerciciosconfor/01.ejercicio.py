texto_usuario = "Hola me llamo Nate, ¿tú cómo te llamas?"
contador_espacios = 0
contador_puntos = 0
contador_comas = 0

for character in texto_usuario:
    if character == " ":
        contador_espacios += 1
    elif character == ".":
        contador_puntos += 1
    elif character == ",":
        contador_comas += 1
    else:
        continue

print(f"""\n
En la frase '{texto_usuario}' existen:

    -Espacios en blanco: {contador_espacios} 
    -Puntos: {contador_puntos}
    -Comas: {contador_comas}
""")