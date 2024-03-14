import random as r

def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    numero = r.randint(1, 10)
    adivina = int(input('Elige un numero del 1 al 10: '))
    if numero == adivina:
        print('Adivinaste!')
    else:
        print('No adivinaste:(')
    
    return