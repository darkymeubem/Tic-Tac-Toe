class OutOfBoundsError(Exception):
    pass

class CellOccupiedError(Exception):
    pass

class Board:
    def __init__(self, size):
        self.size = size
        self.mat = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'O'
        self.turn = 1

    def make_move(self, i, j):
        if not (0 <= i < self.size and 0 <= j < self.size):
            raise OutOfBoundsError("Movimento fora dos limites do tabuleiro!")

        if self.mat[i][j] != ' ':
            raise CellOccupiedError("Esta célula já está ocupada!")

        self.mat[i][j] = self.current_player
        self.current_player = 'X' if self.current_player == 'O' else 'O'
        self.turn += 1
        return True

    def is_full(self):
        return all(cell != " " for row in self.mat for cell in row)

    def check_victory(self):
        size = self.size
        for i in range(size):
            if all(self.mat[i][j] == self.mat[i][0] and self.mat[i][j] != " " for j in range(size)):
                return self.mat[i][0]
        for j in range(size):
            if all(self.mat[i][j] == self.mat[0][j] and self.mat[i][j] != " " for i in range(size)):
                return self.mat[0][j]
        if all(self.mat[i][i] == self.mat[0][0] and self.mat[i][i] != " " for i in range(size)):
            return self.mat[0][0]
        if all(self.mat[i][size - 1 - i] == self.mat[0][size - 1] and self.mat[i][size - 1 - i] != " " for i in range(size)):
            return self.mat[0][size - 1]
        if self.is_full():
            return "Empate"
        return None