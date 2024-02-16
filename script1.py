from math import ceil
import sys

jugador1 = ""
jugador2 = ""
switch = False

# Lleva la cuenta de los sets ganados por cada jugador


def sets():
    global switch
    juegos_ganados = [0, 0]
    while True:
        ganador_game = game()
        juegos_ganados[ganador_game] += 1
        if not switch:
            print(f"Game count: {jugador1} - {juegos_ganados[0]} | | {juegos_ganados[1]} - {jugador2}")
        else:
            print(f"Game count: {jugador2} - {juegos_ganados[1]} | | {juegos_ganados[0]} - {jugador1}")
        if juegos_ganados[0] > 5:
            if abs(juegos_ganados[0] - juegos_ganados[1]) >= 2:
                if ((juegos_ganados[0] + juegos_ganados[1]) % 2) == 1:
                    switch = not switch
                    print("------- CAMBIO DE CANCHA ---------")
                return 0
        if juegos_ganados[1] > 5:
            if abs(juegos_ganados[0] - juegos_ganados[1]) >= 2:
                if ((juegos_ganados[0] + juegos_ganados[1]) % 2) == 1:
                    switch = not switch
                    print("------- CAMBIO DE CANCHA ---------")
                return 1


# Lleva la cuenta del juego


def game():
    scores = [0, 15, 30, 40, "Advantage", "Game"]
    game_score = [0, 0]
    scores_in_a_row = [0, 0]
    while not(game_score[0] == 5 or game_score[1] == 5):
        scored = -1
        while not (scored == 1 or scored == 2):
            try:
                scored = int(input("Ingrese el jugador que anotó (1/2):"))
                if scored != (1 or 2):
                    print("Debes ingresar un 1 ó 2.")
            except ValueError:
                print("Tienes que introducir un número.")
            except UnicodeDecodeError:
                print("Uno de los caracteres ingresados no fue reconocido")
        match scored:
            case 1:
                if scores_in_a_row[0] >= 1 and game_score[0] >= 3:
                    game_score[0] = 5
                else:
                    game_score[0] += 1
                    scores_in_a_row[0] += 1
                    scores_in_a_row[1] = 0
                if game_score[1] == 4:
                    game_score[1] = 3
            case 2:
                if scores_in_a_row[1] >= 1 and game_score[1] >= 3:
                    game_score[1] = 5
                else:
                    game_score[1] += 1
                    scores_in_a_row[1] += 1
                    scores_in_a_row[0] = 0
                if game_score[0] == 4:
                    game_score[0] = 3
        print(f"El jugador {scored} anotó un punto")
        if not switch:
            print(f"Puntaje: {jugador1} - {scores[game_score[0]]} | | {scores[game_score[1]]} - {jugador2}")
        else:
            print(f"Puntaje: {jugador2} - {scores[game_score[1]]} | | {scores[game_score[0]]} - {jugador1}")
    if game_score[0] == 5:
        print(f"El jugador {jugador1} ganó el juego")
        return 0
    else:
        print(f"El jugador {jugador2} ganó el juego")
        return 1


# Lógica principal, termina cuando alguien gana


if __name__ == '__main__':
    sets_a_jugar = 0
    # Verificamos que los nombres de los jugadores sean bien definidos
    while jugador1 == "":
        jugador1 = input("Ingrese el nombre del Jugador 1: ")
    print(f"Jugador 1: {jugador1}")
    while jugador2 == "":
        jugador2 = input("Ingrese el nombre del Jugador 2: ")
    print(f"Jugador 2: {jugador2}")
    # Verificamos que los sets a jugar sean mayor a 0 y no pares
    while sets_a_jugar <= 0 or sets_a_jugar % 2 == 0:
        try:
            sets_a_jugar = int(input("Ingrese el número de sets a jugar: "))
            if sets_a_jugar % 2 == 0:
                print("El número de sets a jugar tiene que ser impar.")
        except ValueError:
            print("Debes ingresar un número")
        except UnicodeDecodeError:
            print("Uno de los caracteres ingresados no fue reconocido")
    set_score = [0, 0]
    while True:
        ganador = sets()
        set_score[ganador] += 1
        print(switch)
        if not switch:
            print(f"Set Count: {jugador1} - {set_score[0]} | | {set_score[1]} - {jugador2}")
        else:
            print(f"Set Count: {jugador2} - {set_score[1]} | | {set_score[0]} - {jugador1}")
        if ceil(sets_a_jugar / 2) == set_score[0]:
            print(f'!!!{jugador1} ganó!!!')
            sys.exit()
        if ceil(sets_a_jugar / 2) == set_score[1]:
            print(f"!!!{jugador2} ganó!!!")
            sys.exit()
