import Board

class Match:
    def __init__(self):
        self.board = Board.Board()
        self.testWin = False
        
        

    def testWin(self, i, j):
            return self.checkHorizontal(i) or self.checkVertical(j) or self.checkDiagonal()
    
    def checkHorizontal(self, i):
        # Verifica a linha 'i' usando um for
        return all(self.board[i][x] == self.currentPlayer for x in range(3))

    def checkVertical(self, j):
        # Verifica a coluna 'j' usando um for
        return all(self.board[x][j] == self.currentPlayer for x in range(3))
    
    def checkDiagonal(self):
        # Verificando as diagonais
        for k in range(3):
            # Verifica a diagonal principal (posição [0,0], [1,1], [2,2]) ou diagonal secundária (posição [0,2], [1,1], [2,0])
            diagonal = [(0, 0), (1, 1), (2, 2)] if i == j else [(0, 2), (1, 1), (2, 0)]
            # Usando operador ternário para verificar as condições
            self.count += 1 if self.board.mat[diagonal[k][0]][diagonal[k][1]] == self.board.currentPlayer else 0
                    
            # Se o contador chegar a 3, retorna True, indicando vitória
            if self.count == 3:
               return True
        return False