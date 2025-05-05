import time
import select
import sys
import random

has_vara = False
has_espada = False

espada = """
   /
  /
 /
O=======[]:::::::::::::::::>
 \\
  \\
   \\
"""

def tiempo_respuesta():
    print("“Resuelve este cálculo mortal:\n"
          "Si tu edad multiplicada por 2, más 13, es igual a 99... ¿cuántos años tienes?”: \n", end='',
          flush=True)
    time.sleep(9)
    print("Tienes 35 segundos para responder esta pregunta\n", end='', flush=True)
    ready, _, _ = select.select([sys.stdin], [], [], 35)

    if ready:
        line = sys.stdin.readline().rstrip('\n')
        return line
    else:
        print("\n¡Se agoto el tiempo, hasta aca llegaste.... JAJAJA!")
        return None

print("\nMAZMORRA FINAL: LA GUARIDA DE EL REY BRUJO DE ANGMAR\n"
      "====================================================\n"
"""
Has seguido el rastro del Rey Brujo hasta las tierras heladas del norte. En lo profundo de un
valle sin nombre se abre la entrada a la última mazmorra: 
El Pozo de Angmar, una prisión antigua, inundada, y custodiada por fuerzas que el tiempo ha olvidado.
""")
time.sleep(8)

print("""
Primera sala: El cruce de los reflejos
--------------------------------------

Dos caminos. En uno, un pedestal con una vara larga de madera.
En el otro, una estatua con una placa rota.
Una inscripción brilla en letras rojas:

“Quien camine sin arma, no podrá blandir el destino.”

Debes elegir:

1) Tomar la vara y cargarla contigo.
2) Ignorarla, confiando en tu ingenio.
""")

option = input("¿Cual eliges valiente caballero: opcion (1)  o opcion (2)\n"
               ">> ")

if option == "1":
    print("Este palo te servirá mas adelante... decidiste bien al tomarlo!\n")
    has_vara = True
else:
    print("Caballero confio en tu ingenio no sera problema para ti... ")

time.sleep(5)

print("""
Segunda sala: El pozo y la espada
---------------------------------
Entras a una caverna donde una espada legendaria yace sumergida en un pozo de agua cristalina.
Un Espiritu ancestral y aterrador aparece y te pregunta con voz desafiante:

"Traes la vara para intentar pescar lo que hay al fondo!"

""")

option = input("Tienes tu vara del cruce de los reflejos? (S) SI o (N) NO\n")

if option == "S":
    if has_vara:
        print("Es Verdad, tienes tu vara, as demostrado coraje y honor. Puedes tomar la espada!\n")
        option = input("Deseas tomar la espada? (S) SI o (N) NO, tu eliges: \n>> ")
        if option == "S":
            print(f"{espada}")
            has_espada = True
        else:
            print("No deseas la espada, quires ver que tan fuerte eres, te puedes arrepentir.\n")
    else:
        print("Es Mentira, no puedes enganarme todo lo veo, no tienes honor, te maldigo a las "
              "profundidades de este pozo\n")
        print("FIN DE TU VIAJE")
        exit()
else:
    respuesta = 43
    print("""
Frente al pozo, un altar con una inscripción mágica:

“Solo quien resuelva el enigma del número sagrado podrá vaciar el pozo.”

Un espíritu ancestral aparece y te dice:
    """)
    time.sleep(10)
    respuesta_caballero = tiempo_respuesta()

    if respuesta_caballero is None:
        print("FIN DE TU VIAJE.... GAME OVER!")
        exit()
    elif respuesta == int(respuesta_caballero):
        print("Vamos al siguiente nivel...")
    else:
        print("Respuesta incorrecta, FIN DE TU VIAJE...")
        exit()

print("""
Tercera sala: El Mago Oscuro
----------------------------

Un Mago tenebroso con voz grave y desafiante bloquea tu camino. Dice:
    “Si traes el palo, tal vez puedas negociar.
    Si traes la espada, me aparto.
    Si no tienes nada... pelearas desarmado.”
    
""")

time.sleep(7)

if has_espada:
    print("Oh.. Tienes la espada legendaria, eres libre de continuar, no podre ganarte...\n")
    time.sleep(5)
elif has_vara:
    print("Tienes la vara, puedes ofrecerla para hacerme un poderoso vaculo\n")
    time.sleep(5)
    option = input("Me entregas tu vara en ofrenda, tu eliges (S) SI o (N) NO: \n>> ")
    if option == "S":
        has_vara = False
        time.sleep(2)
        print("Buena eleccion, salvaste tu vida.. JAJAJA eres un cobarde, pero puedes continuar\n"
              "Dudo que logres llegar al final... \n"
              "Quiero ver que puedes hacer con una simple madera contra el REY BRUJO, la quieres\n"
              "de vuelta... JAJAJA")
        option = input("Toma la madera, elige (S) SI o (N) NO\n")
        if option == "S":
            has_vara = True
            print("No creo que te sirva de mucho esa varita jajaja")
        else:
            print("Quizas tenias una oportunida si aceptabas la madera")
    else:
        time.sleep(2)
        print("Moriras caballero esa vara no te servira.... no eres rival para mi... ¡MUEREEEE!\n")
        exit()
else:
    print("Moriras caballero estas desarmado.... no eres rival para mi... ¡MUEREEEE!\n"
          "Quizas tengas una oportunidad, quieres seguir apostando a tu ingenio: \n"
          )
    time.sleep(3)
    option = input("Tu eliges (S) SI o (N) NO: \n>> ")
    if option == "N":
        print("Hasta termino tu camino... Descansa en paz, necio..\n")
        exit()
    else:
        print("Adivina el numero del 1 al 10, tienes 3 intentos, no falles JAJAJA\n")
        count = 1
        num_random = random.randint(1, 10)
        while count <= 3 or num_random == option:
            option = int(input("Que numero eliges caballero: \n>> "))
            if option == num_random:
                print("Bien hecho, puedes continuar tu viaje... \n")
            elif count == 3:
                print(f"Es tu ultimo intento caballero, {num_random} era el numero, tu fin llego..\n")
                exit()
            elif option < num_random:
                print("Pista: Debes ingresar un numero mayor... buena suerte\n")
                print("Intentalo una vez mas, el fin de tus dias se acerca caballero... JAJAJA\n")
            elif option > num_random:
                print("Pista: Debes ingresar un numero menor... Buena suerte\n")
                print("Intentalo una vez mas, el fin de tus dias se acerca caballero... JAJAJA\n")
            else:
                print("Ingresa un numero intentalo nuevamente\n")

            count += 1

print("""
Sala final: El Trono del Rey Brujo
==================================

Llegas a una cámara de piedra negra. El Rey Brujo está de pie frente a su trono.
No habla. Solo desenfunda su espada de fuego negro.

El resultado depende de tus decisiones anteriores:

Si traes la espada mágica, puedes enfrentarlo en combate justo.

Si no traes la espada pero sí el palo, debes improvisar y defenderte con creatividad.

Si no traes ninguno... quizás solo una última decisión pueda salvarte.


""")

time.sleep(8)
option = input("El Rey Brujo levanta su espada.“¿Lucharás… o te arrodillarás?”\n"
               "Tu eliges: (L) Luchare, (A) Me Arrodillare\n>>>")

if option == "L":
    if has_espada:
        print("Tienes la espada legendaria, tendremos una buena batalla...!\n")
        print("Me derrotaste, fue una buena batalla... \n")
        print("GANASTE, ERES EL VENCEDOR...")
        exit()
    elif has_vara:
        ataque_rey_brujo = random.randint(1, 3)
        print("No eres rival para mi con esa madera, eres una presa facil\n"
              "El rey brujo te ataca adivina el golpe: \n")
        option = int(input("Te atacara arriba (1) , abajo (2) o al medio (3) "))
        if ataque_rey_brujo == option:
            print("Eres un gran gerreo esquivaste mi ataque... \n")
            print("Me venciste... noooooo\n")
            print("GANASTE, ERES EL VENCEDOR...")
            exit()
        else:
            print(f"Perdiste caballero no tienes nada que hacer... tu fin a llegado\n")
            exit()
    else:
        print("Vienes desarmado jajaja, no tienes oportunidad.... MUEREEEE!\n")
        print("TU FIN LLEGO\n")
        exit()
elif option == "A":
    print("COBARDE... no tienes orgullo... es tu fin!\n")
    print("PERDISTE no tienes honor...\n")
    exit()
else:
    print("El miedo esta en tus huesos, no supiste elegir, fin del juego")
    exit()


