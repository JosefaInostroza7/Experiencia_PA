import random

def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    numero = random.randint(1, 10)
    opcion = input("Es par o impar: ")
    while opcion not in ("par", "impar", "Par", "Impar"):
        print("opcion invalida, vuelva a escribir")
        opcion = input("Es par o impar: ")
    if numero % 2 == 0:
        es_par = True
    else:
        es_par = False
    if es_par and opcion in ("par", "Par"):
        print(f"adivinaste! el numero era: {numero}")
    elif es_par == False and opcion in ("impar", "Impar"):
        print(f"adivinaste! el numero era: {numero}")
    else:
        print(f"no adivinaste :( el numero era {numero}")
    