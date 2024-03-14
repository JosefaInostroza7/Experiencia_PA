import random as r

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    termino = False
    while termino == False:
        compu = r.choice(['piedra', 'papel', 'tijera'])
        inputt = 0
        while inputt == 0:
            user = input('Elige piedra, papel o tijera: ')
            if user in ['piedra', 'papel', 'tijera']:
                inputt = 1
            else:
                print('Intenta de nuevo por favor.')


        if user == 'piedra' and compu == 'papel':
            print('El computador hizo papel.\n Has perdido :(')
            termino = True

        elif user == 'piedra' and compu == 'tijera':
            print('El computador hizo tijera.\n Has ganado :)')
            termino = True

        elif user == 'papel' and compu == 'tijera':
            print('El computador hizo tijera.\n Has perdido :(')
            termino = True

        elif user == 'papel' and compu == 'piedra':
            print('El computador hizo piedra.\n Has ganado :)')
            termino = True

        elif user == 'tijera' and compu == 'piedra':
            print('El computador hizo piedra.\n Has perdido :(')
            termino = True

        elif user == 'tijera' and compu == 'papel':
            print('El computador hizo papel.\n Has ganado :)')
            termino = True

        print('Empate, ¡sigue jugando!')