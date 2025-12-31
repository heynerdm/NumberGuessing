import json
import click
from pathlib import Path
import random


# FUNCIONES

#GENERA EL NUMERO ALEATORIO
def generaterandom():

    rndnum = random.randint(1,100)
    return rndnum


#CONFIRMA SI EL NUMERO ES EL CORRECTO
def confirmar(numero,numeropersona):
    if numeropersona == numero:
        return True
    else:
        return False

#AYUDA A ELEGIR LA DIFICULTAD
def obtener_dificultad(nivel):
    if nivel == 1:
        dificultad_numero = 10
        print('Great! You have selected the Easy difficulty level.\nLet\'s start the game!')
    elif nivel == 2:
        dificultad_numero = 5
        print('Great! You have selected the Medium difficulty level.\nLet\'s start the game!')
    elif nivel == 3:
        dificultad_numero = 3
        print('Great! You have selected the Hard difficulty level.\nLet\'s start the game!')
    else:
        dificultad_numero = 5
        print('Invalid selection. Defaulting to Medium difficulty.\nLet\'s start the game!')

    return dificultad_numero


#LA LOGICA DEL JUEGO
def mecanica(intentos):
    numero_random = generaterandom()

    for i in range(1, intentos + 1):
        try:
            respuesta = int(input(f'Intento {i}/{intentos} - Escribe tu respuesta: '))
        except ValueError:
            print('Entrada inválida. Por favor introduce un número entero.')
            continue

        if confirmar(numero_random, respuesta):
            print(f'Congratulations! You guessed the correct number in {i} attempt(s).')
            break
        elif respuesta > numero_random:
            print(f'Incorrect! The number is less than: {respuesta}')
        else:
            print(f'Incorrect! The number is greater than: {respuesta}')
    else:
        print(f'Sorry, you did not guess the number. The correct number was {numero_random}.')

#CLI

@click.group()
def main():
    """Adivina el Numero Game CLI."""
    pass

@main.command()
@click.option('--dificultad', 'nivel', type=int, prompt='Selecciona la dificultad (1-Easy, 2-Medium, 3-Hard)', help='Dificultad del juego')
def jugar(nivel):
    dificultad_numero = obtener_dificultad(nivel)
    mecanica(dificultad_numero)

if __name__ == '__main__':
    main()




