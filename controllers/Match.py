import os
from controllers.Board import Board

class OutOfBoundsError(Exception):
    """Exceção levantada quando uma jogada é feita fora dos limites do tabuleiro."""
    pass

class CellOccupiedError(Exception):
    """Exceção levantada quando uma célula já está ocupada."""
    pass

class Match:
    def __init__(self):
        self.board = Board()
        self.winner = None  # Armazena o vencedor (X, O ou Empate)
        self.game_over = False  # Variável de controle para o loop principal

    def play(self):
        """Inicia o jogo."""
        print("Bem-vindo ao Tic-Tac-Toe!")

        while not self.game_over:
            os.system("clear")  # Limpa o terminal
            self.board.printBoard()

            cor = "\033[1;34m" if self.board.currentPlayer == 'O' else "\033[1;31m"
            print(f"Jogador {cor}{self.board.currentPlayer}\033[m, faça seu movimento!\nTurno: {self.board.turn}")

            try:
                linha = int(input("Informe a linha (1-3): ")) - 1
                coluna = int(input("Informe a coluna (1-3): ")) - 1

                self.board.makeMove(linha, coluna)  # Tenta fazer o movimento

                self.winner = self.board.check_victory() # Verifica o vencedor após cada jogada
                if self.winner:
                    self.game_over = True
                    os.system("clear")
                    self.board.printBoard()
                    if self.winner == "Empate":
                        print("Empate! Jogo encerrado.")
                    else:
                        print(f"Jogador {cor}{self.winner}\033[m, venceu!")
                    break

            except OutOfBoundsError as e:
                print(e)
            except CellOccupiedError as e:
                print(e)
            except ValueError:
                print("Entrada inválida. Por favor, insira números inteiros.")

        print("Jogo encerrado. Obrigado por jogar!")