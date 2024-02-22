from random import randint

POINT_STR="Ingrese el ganador del punto:\n1\n2\n"
ERROR_STR="Ingrese 1 o 2 exclusivamente"
POINT_DCT={0:"0", 1:"15", 2:"30", 3:"40", 4:"Adv"}


if __name__ == '__main__':
    #Primero necesito el nombre de los jugadores.
    jug1, jug2 = input("Ingrese el nombre del Jugador 1\n"), input("Ingrese el nombre del jugador 2\n")
    #Necesito llevar la cuenta de los sets que llevan ambos jugadores.
    s1, s2 = 0, 0
    #Anuncio que empieza el juego, que pueden empezar a jugar.
    #Para esto, necesito empezar la cuenta de juegos y la cuenta de puntos.
    j1, p1, j2, p2 = 0, 0, 0, 0
    #Como se tiene que anunciar el saque, tengo que escoger un jugador
    #al azar para que empieze a sacar.
    if randint(0, 2) == 0:
        saque = jug1
    else:
        saque = jug2
    print(f"Empezará sacando: {saque}")
    #Repetiré lo siguiente hasta que s1 o s2 == 2
    game, sset = False, False
    while s1 < 2 and s2 < 2:
        try:
            point = int(input(POINT_STR)) #Que ingresen al ganador del punto.
            if point == 1: #J1 hizo un punto.
                #Si el J1 tiene puntos menores o iguales a 30, nada, p1++
                if p1 <= 2:
                    p1 += 1
                elif p1 == 3: #Estoy en 40.
                    if p2 == 4: #El marcador era 40-Adv.
                        p2 -= 1
                    elif p2 == 3: #El marcador era 40-40.
                        p1 += 1
                    else:
                        #El j1 ha hecho un juego y debe de ser notificado.
                        p1, p2 = 0, 0
                        j1 += 1
                        game = True
                        print(f"Juego: {jug1}")
                else: #Estoy en Adv y hago un punto, entonces juego automático.
                    p1, p2 = 0, 0
                    j1 += 1
                    game = True
                    print(f"Juego: {jug1}")
            elif point == 2: #J2 hizo un punto, mismos casos pero en espejo.
                if p2 <= 2:
                    p2 += 1
                elif p2 == 3: #Estoy en 40.
                    if p1 == 4: #El marcador era 40-Adv.
                        p1 -= 1
                    elif p1 == 3: #El marcador era 40-40.
                        p2 += 1
                    else:
                        #El j2 ha hecho un juego y debe de ser notificado.
                        p1, p2 = 0, 0
                        j2 += 1
                        game = True
                        print(f"Juego: {jug2}")
                else: #Estoy en Adv y hago un punto, entonces juego automático.
                    p1, p2 = 0, 0
                    j2 += 1
                    game = True
                    print(f"Juego: {jug2}")
            else:
                print(ERROR_STR)
                continue
            #Se termina de procesar el punto.
            #ahora hay que anunciar el marcador.
            if not game:
                print(f"{jug1} {POINT_DCT[p1]} - {POINT_DCT[p2]} {jug2}")
            else:
                print(f"{jug1} {j1} - {j2} {jug2}")
            #Como algún jugador pudo haber hecho un juego, usaremos una bandera
            #para notificarlo
            if game:
                #Hay que hacer el cambio de saque.
                if saque == jug1:
                    saque = jug2
                else:
                    saque = jug1
                print(f"Saque: {saque}")
                #Hay que verificar el cambio de cancha.
                if (j1 + j2) % 2 == 1:
                    print("Cambio de cancha")
                #Alguien pudo haber hecho un set
                if (j1 >= 6 or j2 >= 6) and abs(j1 - j2) >= 2:
                    sset = True
                game = False #Para no volver a hacer este procesamiento.
            if sset: #Alguien hizo un set
                if max(j1, j2) == j1: #J1 tiene la mayoría de juegos.
                    s1 += 1
                    print(f"Set: {jug1}")
                else:
                    s2 += 1
                    print(f"Set: {jug2}")
                print(f"{s1} sets a {s2}")
                j1, j2 = 0, 0 #Se reinician los juegos.
                sset = False #Para no volver a procesar esto
        except ValueError:
            print(ERROR_STR)
    if s1 == 2:
        print(f"Ganador: {jug1}")
    else:
        print(f"Ganador: {jug2}")
