


class Board:
    def __init__(self):
        self.player = Player()
        self.currentPlayer = self.player.P1
        self.currentPlayer = 'O'  # Presumo que o jogador inicial seja 'O'
        self.mat = [[' ' for _ in range(3)] for _ in range(3)]  # Matriz 3x3 para o tabuleiro
        self.turn = 1
        

    def makeMove(self, i, j):
        if self.validateMove(i, j) and self.validatePosition(i, j):
            self.mat[i][j] = self.currentPlayer
            self.currentPlayer = self.player if self.currentPlayer == self.player.P2 else self.player.P2
            self.turn += 1

    def validateMove(self, i, j):
        if 0 <= i < 3 and 0 <= j < 3:  # Verifica se os índices estão dentro dos limites
            return True
        return False

    def validatePosition(self, i, j):
        if (self.mat[i][j]):
            return False  # Se a posição já estiver ocupada
        return True
    def oponente(self):
        return self.player.P2 if self.currentPlayer == self.player.P1 else self.player.P1

     
class Player:
    def __init__(self):
        self.P1 = 'O'
        self.P2 = 'X'
    