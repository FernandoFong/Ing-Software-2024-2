def marcador(jugador1, jugador2):
    print("Marcador:")
    print(f"{jugador1['nombre']}: Juegos ganados = {jugador1['juegos']}, Sets ganados = {jugador1['sets']}")
    print(f"{jugador2['nombre']}: Juegos ganados = {jugador2['juegos']}, Sets ganados = {jugador2['sets']}")
    print("Puntuación actual:", puntuacion(jugador1['puntos']), "-", puntuacion(jugador2['puntos']))
    print()

def puntuacion(puntos):
    if puntos == 0:
        return "0"
    elif puntos == 1:
        return "15"
    elif puntos == 2:
        return "30"
    elif puntos == 3:
        return "40"
    else:
        return "Ventaja"

def juego(jugador1, jugador2):
    while True:
        try:
            opcion = int(input(f"¿Quién ganó el punto? (1 para {jugador1['nombre']} /-\ 2 para {jugador2['nombre']} / 0 para Salir): "))
            if opcion == 0:
                break
            elif opcion == 1:
                jugador1['puntos'] += 1
            elif opcion == 2:
                jugador2['puntos'] += 1
            else:
                print("Opción no válida. Por favor, ingresa '1', '2' o '0'.")
                continue

            if jugador1['puntos'] >= 4 and jugador1['puntos'] >= jugador2['puntos'] + 2:
                jugador1['juegos'] += 1
                jugador1['puntos'] = 0
                jugador2['puntos'] = 0
            elif jugador2['puntos'] >= 4 and jugador2['puntos'] >= jugador1['puntos'] + 2:
                jugador2['juegos'] += 1
                jugador1['puntos'] = 0
                jugador2['puntos'] = 0
            elif jugador1['puntos'] == 3 and jugador2['puntos'] == 3:
                print("Deuce! Puntos igualados a 40-40.")
            elif jugador1['puntos'] >= 4 and jugador2['puntos'] >= 4:
                if jugador1['puntos'] == jugador2['puntos'] + 1:
                    print("Ventaja Jugador 1!")
                elif jugador2['puntos'] == jugador1['puntos'] + 1:
                    print("Ventaja Jugador 2!")

            marcador(jugador1, jugador2)

            if (jugador1['juegos'] >= 6 and jugador1['juegos'] >= jugador2['juegos'] + 2) or (jugador2['juegos'] >= 6 and jugador2['juegos'] >= jugador1['juegos'] + 2):
                if jugador1['juegos'] > jugador2['juegos']:
                    jugador1['sets'] += 1
                    print(f"{jugador1['nombre']} ha ganado el set.")
                else:
                    jugador2['sets'] += 1
                    print(f"{jugador2['nombre']} ha ganado el set.")
                jugador1['juegos'] = 0
                jugador2['juegos'] = 0
                marcador(jugador1, jugador2)
                break

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


def set(jugador1, jugador2):
    while True:
        try:
            juego(jugador1, jugador2)

            if (jugador1['juegos'] >= 6 and jugador1['juegos'] >= jugador2['juegos'] + 2) or (jugador2['juegos'] >= 6 and jugador2['juegos'] >= jugador1['juegos'] + 2):
                if jugador1['juegos'] > jugador2['juegos']:
                    jugador1['sets'] += 1
                    print(f"{jugador1['nombre']} ha ganado el set.")
                else:
                    jugador2['sets'] += 1
                    print(f"{jugador2['nombre']} ha ganado el set.")
                jugador1['juegos'] = 0
                jugador2['juegos'] = 0

                print("¡Set completado!")
                marcador(jugador1, jugador2)

            if jugador1['sets'] == 3:
                print(f"{jugador1['nombre']} ha ganado el juego.")
                break
            elif jugador2['sets'] == 3:
                print(f"{jugador2['nombre']} ha ganado el juego.")
                break

            if (jugador1['juegos'] + jugador2['juegos']) % 2 != 0:
                print("¡Cambio de cancha!")

            opcion = input("¿Continuar al siguiente set? (Si / No): ").lower()
            if opcion != "si":
                break
        except Exception as e:
            print("Error:", e)
            print("Se ha producido un error. Reiniciando el juego.")
            jugador1['puntos'] = 0
            jugador2['puntos'] = 0
            jugador1['juegos'] = 0
            jugador2['juegos'] = 0
            jugador1['sets'] = 0
            jugador2['sets'] = 0

if __name__ == "__main__":
    print("¡Bienvenido al marcador de tenis!")
    nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")
    nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")

    jugador1 = {'nombre': nombre_jugador1, 'puntos': 0, 'juegos': 0, 'sets': 0}
    jugador2 = {'nombre': nombre_jugador2, 'puntos': 0, 'juegos': 0, 'sets': 0}

    print("Presiona enter para comenzar el juego.")
    input()

    set(jugador1, jugador2)








