class OutOfBoundsError(Exception):
    pass

class CellOccupiedError(Exception):
    pass

class Board:
    def __init__(self):
        self.mat = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'
        self.turn = 1

    def make_move(self, i, j):  # Nome consistente: make_move
        if not (0 <= i < 3 and 0 <= j < 3):
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
        for i in range(3):
            if self.mat[i][0] == self.mat[i][1] == self.mat[i][2] != " ":
                return self.mat[i][0]
            if self.mat[0][i] == self.mat[1][i] == self.mat[2][i] != " ":
                return self.mat[0][i]

        if self.mat[0][0] == self.mat[1][1] == self.mat[2][2] != " ":
            return self.mat[0][0]
        if self.mat[0][2] == self.mat[1][1] == self.mat[2][0] != " ":
            return self.mat[0][2]

        if self.is_full():
            return "Empate"

        return None