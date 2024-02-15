class TennisMatch:
    POINTS = {0: "0", 1: "15", 2: "30", 3: "40", 4: "game"}
    SCORE_NAMES = {0: "0", 1: "15", 2: "30", 3: "40"}

    def __init__(self, player1, player2, sets_to_win=3):
        try:
            if sets_to_win % 2 == 0:
                raise ValueError("El número de sets debe ser impar.")
            self.player1 = player1
            self.player2 = player2
            self.sets_to_win = sets_to_win
            self.player1_score = 0
            self.player2_score = 0
            self.player1_sets_won = 0
            self.player2_sets_won = 0
            self.current_set = [0, 0]  # Player1 games, Player2 games
            self.current_serving_player = 1  # Player1 serves first
            self.games_played_in_set = 0  # Track number of games played in current set
            self.change_of_serve = True  # Flag to track the change of serve
        except ValueError as e:
            print("Error:", "El número de sets debe ser impar.")

    def score_point(self, player):
        try:
            if player == 1:
                self.player1_score += 1
            elif player == 2:
                self.player2_score += 1
            self.update_game_score()
        except Exception as e:
            print("Error:", e)

    def update_game_score(self):
        try:
            if self.player1_score == 4 and self.player2_score == 4:
                # Deuce
                self.player1_score = 3
                self.player2_score = 3
            elif self.player1_score >= 4 and self.player1_score - self.player2_score >= 2:
                # Player 1 wins game
                self.current_set[0] += 1
                self.player1_sets_won += 1
                self.games_played_in_set += 1
                self.player1_score = 0
                self.player2_score = 0
                print(f"{self.player1} gana el juego!")
                self.change_of_serve = True
            elif self.player2_score >= 4 and self.player2_score - self.player1_score >= 2:
                # Player 2 wins game
                self.current_set[1] += 1
                self.player2_sets_won += 1
                self.games_played_in_set += 1
                self.player1_score = 0
                self.player2_score = 0
                print(f"{self.player2} gana el juego!")
                self.change_of_serve = True
        except Exception as e:
            print("Error:", e)

    def change_server(self):
        try:
            if self.change_of_serve:
                self.current_serving_player = 3 - self.current_serving_player
                self.change_of_serve = False
        except Exception as e:
            print("Error:", e)

    def change_court(self):
        try:
            if self.games_played_in_set % 2 != 0:
                print("Cambiando lados de la cancha.")
                self.change_of_serve = True
        except Exception as e:
            print("Error:", e)

    def print_score(self):
        try:
            print(f"Marcador actual del set: {self.current_set[0]}-{self.current_set[1]}")
            print(f"Marcador actual del juego: {self.POINTS[self.player1_score]}-{self.POINTS[self.player2_score]}")
            print(f"Sirviendo: Jugador {self.current_serving_player}")
        except Exception as e:
            print("Error:", e)

    def check_set_winner(self):
        try:
            if max(self.current_set) == 6 and abs(self.current_set[0] - self.current_set[1]) >= 2:
                return True
            return False
        except Exception as e:
            print("Error:", e)

    def play_point(self):
        try:
            player = int(input(f"¿Quién ganó el punto? Ingresa 1 para {self.player1} o 2 para {self.player2}: "))
            if player not in [1, 2]:
                raise ValueError("Por favor, elige 1 o 2")
            self.score_point(player)
            self.change_server()
            self.change_court()
            self.print_score()
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Error:", e)

    def play_match(self):
        try:
            while max(self.current_set) < (self.sets_to_win // 2 + 1):
                self.play_point()
                if self.check_set_winner():
                    print("¡Set ganado! Cambiando lados de la cancha.")
                    self.current_set = [0, 0]
                    self.games_played_in_set = 0
                    self.player1_sets_won += 1 if self.current_set[0] > self.current_set[1] else 0
                    self.player2_sets_won += 1 if self.current_set[1] > self.current_set[0] else 0
                    if self.player1_sets_won == (self.sets_to_win // 2 + 1):
                        print(f"{self.player1} gana el partido!")
                        break
                    elif self.player2_sets_won == (self.sets_to_win // 2 + 1):
                        print(f"{self.player2} gana el partido!")
                        break

            if self.player1_sets_won > self.player2_sets_won:
                print(f"{self.player1} gana el partido!")
            elif self.player2_sets_won > self.player1_sets_won:
                print(f"{self.player2} gana el partido!")
            else:
                print("El partido termina en empate.")
        except Exception as e:
            print("Error:", e)

# Programa principal
if __name__ == "__main__":
    try:
        player1_name = input("Ingresa el nombre del jugador 1: ")
        player2_name = input("Ingresa el nombre del jugador 2: ")
        sets_to_win = int(input("Ingresa el número de sets para ganar: "))
        match = TennisMatch(player1_name, player2_name, sets_to_win)
        match.play_match()
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)