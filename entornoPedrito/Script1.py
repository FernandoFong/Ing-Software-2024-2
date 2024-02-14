class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.juegos = 0
        self.sets = 0

    def reiniciar_puntos(self):
        self.puntos = 0

    def reiniciar_juegos(self):
        self.juegos = 0


def imprimir_puntos(nombre, puntos):
    if puntos == 0:
        print(nombre, ": 0")
    elif puntos == 1:
        print(nombre, ": 15")
    elif puntos == 2:
        print(nombre, ": 30")
    elif puntos >= 3:
        print(nombre, ": 40")

def pedirPuntos():
    while True:
        try:
            seleccionPuntos = int(
                input(f"Ingrese quien anota el punto. (1 para jugador1 y 2 para jugador2): "))
            if seleccionPuntos == 1 or seleccionPuntos == 2:
                return seleccionPuntos
        except ValueError:
            print("Debes ingresar 1 o 2, no una cadena")


def main():
    nombre1 = input("Por favor, ingresa el nombre del jugador 1: ")
    nombre2 = input("Por favor, ingresa el nombre del jugador 2: ")
    jugador1 = Jugador(nombre1)
    jugador2 = Jugador(nombre2)

    # Variable para controlar quién tiene el saque (1 para jugador1, 2 para jugador2)
    saque = 1

    while jugador1.sets < 2 and jugador2.sets < 2:  # Gana el mejor de 3

        ganadorJuego = False
        while ganadorJuego == False:  # gana quien primero llegue a 6 juegos y la diferencia sea de al menos 2, sino continua
            if ((jugador1.juegos >= 6) or (jugador2.juegos >= 6)) and (
                    abs(jugador1.juegos - jugador2.juegos) >= 2):
                ganadorJuego = True
            else:
                ganadorPuntos = False
                while ganadorPuntos == False:  # gana quien primero que llege a 4 puntos y la direncia sea al menos de 2, sino continua
                    if ((jugador1.puntos >= 4) or (jugador2.puntos >= 4)) and (
                            abs(jugador1.puntos - jugador2.puntos) >= 2):
                        ganadorPuntos = True
                    else:
                        # Se entra en el caso de que el partido se ha empatado o hay ventaja
                        if jugador1.puntos >= 3 and jugador2.puntos >= 3:

                            puntuador = pedirPuntos()
                            if puntuador == 1:
                                jugador1.puntos += 1
                                if (jugador1.puntos > jugador2.puntos):
                                    print("--- ", jugador1.nombre, " ADVANTAGE ---")
                                    imprimir_puntos(jugador2.nombre, jugador2.puntos)
                                else:
                                    imprimir_puntos(jugador1.nombre, jugador1.puntos)
                                    imprimir_puntos(jugador2.nombre, jugador2.puntos)
                            elif puntuador == 2:
                                jugador2.puntos += 1
                                if jugador1.puntos < jugador2.puntos:
                                    imprimir_puntos(jugador1.nombre, jugador1.puntos)
                                    print("--- ", jugador2.nombre, " ADVANTAGE ---")
                                else:
                                    imprimir_puntos(jugador1.nombre, jugador1.puntos)
                                    imprimir_puntos(jugador2.nombre, jugador2.puntos)

                        else:
                            puntuador = pedirPuntos()
                            if puntuador == 1:
                                jugador1.puntos += 1
                                imprimir_puntos(jugador1.nombre, jugador1.puntos)
                                imprimir_puntos(jugador2.nombre, jugador2.puntos)
                            elif puntuador == 2:
                                jugador2.puntos += 1
                                imprimir_puntos(jugador1.nombre, jugador1.puntos)
                                imprimir_puntos(jugador2.nombre, jugador2.puntos)

                if jugador1.puntos > jugador2.puntos:  # aumenta partidas ganadas al jugador e imprimir quien ha ganado
                    jugador1.juegos += 1
                    print(jugador1.nombre,  "HA GANADO EL JUEGO.  \n")
                    jugador1.reiniciar_puntos()
                    jugador2.reiniciar_puntos()
                else:
                    jugador2.juegos += 1
                    print(jugador2.nombre, " HA GANADO EL JUEGO.\n")
                    jugador1.reiniciar_puntos()
                    jugador2.reiniciar_puntos()

                print(
                    "\nMARCADOR JUEGOS")  # imprime el marcador de los juegos ganados de cada jugador
                print(jugador1.nombre, ": ", jugador1.juegos, "- ", jugador2.juegos,
                      ": ", jugador2.nombre)

                # Imprimir quién tiene el saque
                print("SAQUE:", jugador1.nombre if saque == 1 else jugador2.nombre)

                # Si un jugador gana el juego, el otro jugador tendrá el saque en el próximo juego
                saque = 1 if saque == 2 else 2

            # si la suma de los juegos es impar, entonces los jugadores cambian de cancha
            if ((jugador2.juegos + jugador1.juegos) % 2 == 1 and (
                    jugador1.juegos - jugador2.juegos != 2)):
                print("-- LOS JUGADORES CAMBIAN DE CANCHA. --\n")

        # aumenta sets ganados al jugador y dice quien ha ganado el set.
        if jugador1.juegos > jugador2.juegos:
            jugador1.sets += 1
            print(jugador1.nombre, " HA GANADO EL SET")
            print(jugador1.nombre, ": ", jugador1.sets, " - ", jugador2.sets, ": ",
                  jugador2.nombre)
            jugador1.reiniciar_juegos()
            jugador2.reiniciar_juegos()
        else:
            jugador2.sets += 1

            print(jugador2.nombre, " HA GANADO EL SET")
            print(jugador1.nombre, ": ", jugador1.sets, " - ", jugador2.sets, ": ",
                  jugador2.nombre)
            jugador1.reiniciar_juegos()
            jugador2.reiniciar_juegos()

    # VERIFICA QUIEN ES EL MEJOR DE 3 SETS, TERMINA EL PARTIDO Y DICE QUIEN ES EL GANADOR
    if jugador1.sets > jugador2.sets:
        print("\n------ EL JUEGO HA TERMINADO -----\n")
        print(jugador1.nombre, " HA GANADO EL PARTIDO")
    else:
        print("\n------ EL JUEGO HA TERMINADO -----\n")
        print(jugador2.nombre, " HA GANADO EL PARTIDO")


if __name__ == '__main__':
    main()