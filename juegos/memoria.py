import random

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    cantidad_numeros = random.randint(1, 5)
    lista_numeros = []
    while cantidad_numeros > 0:
        lista_numeros.append(random.randint(1, 100))
        cantidad_numeros -= 1
    print(f"los numeros son: {lista_numeros}")
    lista_jugador = []
    print("ahora repita la secuencia, ingresando un numero a la vez:")
    for numero_act in range(len(lista_numeros)):
        lista_numeros[numero_act] = str(lista_numeros[numero_act])
        numero_jugador = input()
        lista_jugador.append(numero_jugador)

    print(f"secuencia original: {lista_numeros}")
    print(f"secuencia jugador: {lista_jugador}")
    if lista_numeros == lista_jugador:
        print("ganaste")
    else:
        print("perdiste")
    return