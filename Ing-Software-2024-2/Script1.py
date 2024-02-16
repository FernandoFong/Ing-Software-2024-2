class MarcadorTenis:
    def __init__(self, sets_para_ganar, nombre_jugador1, nombre_jugador2):
        self.sets_para_ganar = sets_para_ganar
        self.nombre_jugador1 = nombre_jugador1
        self.nombre_jugador2 = nombre_jugador2
        self.marcador_jugador1 = 0
        self.marcador_jugador2 = 0
        self.sets_jugador1 = 0
        self.sets_jugador2 = 0
        self.juegos_en_set = 0
        self.cambio_cancha = False

    def marcar_punto(self, jugador):
        if jugador not in [1, 2]:
            raise ValueError("El número de jugador debe ser 1 o 2")

        if self.sets_jugador1 == self.sets_para_ganar or self.sets_jugador2 == self.sets_para_ganar:
            print(f"¡{self.obtener_ganador()} ya ganó el partido!")
            return

        if self.cambio_cancha:
            self.cambio_cancha = False
            print("Cambio de cancha.")

        if jugador == 1:
            self.marcador_jugador1 += 1
        elif jugador == 2:
            self.marcador_jugador2 += 1

        if self.marcador_jugador1 == 4 and self.marcador_jugador2 == 4:
            self.juegos_en_set += 1
            if self.juegos_en_set % 2 != 0:
                self.cambio_cancha = True
            if self.juegos_en_set % 2 == 0:
                self.ganar_juego(0)
            else:
                print("Ventaja - Ventaja")
        elif self.marcador_jugador1 >= 4 and self.marcador_jugador1 - self.marcador_jugador2 >= 2:
            self.ganar_juego(1)
        elif self.marcador_jugador2 >= 4 and self.marcador_jugador2 - self.marcador_jugador1 >= 2:
            self.ganar_juego(2)
        else:
            print(self.obtener_marcador())

    def ganar_juego(self, jugador):
        if jugador == 1:
            self.marcador_jugador1 = 0
            self.marcador_jugador2 = 0
            self.juegos_en_set += 1
            if self.juegos_en_set % 2 != 0:
                self.cambio_cancha = True
            if self.juegos_en_set % 2 == 0 and self.juegos_en_set // 2 >= 6:
                self.ganar_set(1)
            else:
                print(f"Juego para {self.nombre_jugador1}")
        elif jugador == 2:
            self.marcador_jugador1 = 0
            self.marcador_jugador2 = 0
            self.juegos_en_set += 1
            if self.juegos_en_set % 2 != 0:
                self.cambio_cancha = True
            if self.juegos_en_set % 2 == 0 and self.juegos_en_set // 2 >= 6:
                self.ganar_set(2)
            else:
                print(f"Juego para {self.nombre_jugador2}")

    def ganar_set(self, jugador):
        if jugador == 1:
            self.sets_jugador1 += 1
        elif jugador == 2:
            self.sets_jugador2 += 1

        print(f"¡{self.obtener_ganador()} gana el set!")

        if self.sets_jugador1 == self.sets_para_ganar or self.sets_jugador2 == self.sets_para_ganar:
            print(f"¡{self.obtener_ganador()} gana el partido!")
        else:
            self.juegos_en_set = 0
            print(self.obtener_marcador())

    def obtener_ganador(self):
        return self.nombre_jugador1 if self.sets_jugador1 > self.sets_jugador2 else self.nombre_jugador2

    def obtener_marcador(self):
        return f"Sets: {self.sets_jugador1}-{self.sets_jugador2}, Juegos: {self.juegos_en_set}, " \
               f"Marcador actual: {self.nombre_jugador1} {self.convertir_marcador(self.marcador_jugador1)} - " \
               f"{self.nombre_jugador2} {self.convertir_marcador(self.marcador_jugador2)}"

    @staticmethod
    def convertir_marcador(puntos):
        if puntos == 0:
            return "0"
        elif puntos == 1:
            return "15"
        elif puntos == 2:
            return "30"
        elif puntos == 3:
            return "40"
        else:
            return "Juego"


# Uso del script
try:
    nombre_jugador1 = input("Ingrese el nombre del jugador 1: ")
    nombre_jugador2 = input("Ingrese el nombre del jugador 2: ")
    sets_para_ganar = int(input("Ingrese el número de sets para ganar el partido (debe ser impar): "))
    if sets_para_ganar % 2 == 0:
        raise ValueError("El número de sets para ganar debe ser impar.")

    marcador = MarcadorTenis(sets_para_ganar, nombre_jugador1, nombre_jugador2)

    while True:
        try:
            jugador_que_gana = int(input(
                f"Ingrese el número del jugador que gana el punto (1 para {nombre_jugador1}, 2 para {nombre_jugador2}): "))
            marcador.marcar_punto(jugador_que_gana)
        except ValueError:
            print("Error: Ingrese un número válido de jugador (1 o 2).")
except KeyboardInterrupt:
    print("\nJuego interrumpido.")
except Exception as e:
    print(f"Error: {str(e)}")