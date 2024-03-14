import random

def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    suma_jugador = 0
    suma_pc = 0
    while suma_jugador < 30 and suma_pc < 30:
        input("presione enter para lanzar su dado: " )
        suma_jugador += random.randint(1,6)
        if suma_jugador < 30:
            suma_pc += random.randint(1,6)
        print(f"suma actual jugador: {suma_jugador}")
        print(f"suma actual pc: {suma_pc}")
    print("termino el juego")
    if suma_jugador >= 30:
        print("gana el jugador")
    else:
        print("perdiste, gana la computadora")

    return