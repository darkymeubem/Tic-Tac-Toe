class OutOfBoundsError(Exception):
    """Exceção levantada quando uma jogada é feita fora dos limites do tabuleiro."""
    pass

class CellOccupiedError(Exception):
    """Exceção levantada quando uma célula já está ocupada."""
    pass

class Board:
    def __init__(self):
        self.mat = [[' ' for _ in range(3)] for _ in range(3)]
        self.currentPlayer = 'O'
        self.turn = 1

    def makeMove(self, i, j):
        """Faz o movimento no tabuleiro e lança exceções se inválido."""
        if not self.validateMove(i, j):
            raise OutOfBoundsError("Movimento fora dos limites do tabuleiro!")  # Lança exceção se fora dos limites

        if self.mat[i][j] != ' ':
            raise CellOccupiedError("Esta célula já está ocupada!")  # Lança exceção se a célula já estiver ocupada

        # Realiza o movimento
        self.mat[i][j] = self.currentPlayer
        self.currentPlayer = 'X' if self.currentPlayer == 'O' else 'O'
        self.turn += 1
        return True  # Movimento válido

    def validateMove(self, i, j):
        """Valida se a jogada está dentro dos limites do tabuleiro."""
        return 0 <= i < 3 and 0 <= j < 3

    def isFull(self):
        """Verifica se o tabuleiro está cheio."""
        return all(cell != " " for row in self.mat for cell in row)

    def printBoard(self):
        """Exibe o tabuleiro com 3 colunas separadas por | e linha pontilhada abaixo de cada linha"""
        for i, row in enumerate(self.mat):
            row_str = f"| {' | '.join(row)} |"
            print(row_str)
            if i < 2:
                print("-" * len(row_str))  # Linha separadora após cada linha, exceto a última

    def check_victory(self):
        """Verifica se há um vencedor e retorna o símbolo ('X' ou 'O') ou None se não houver."""
        for i in range(3):
            # Verifica linhas
            if self.mat[i][0] == self.mat[i][1] == self.mat[i][2] != " ":
                return self.mat[i][0]  # Retorna o símbolo vencedor

            # Verifica colunas
            if self.mat[0][i] == self.mat[1][i] == self.mat[2][i] != " ":
                return self.mat[0][i]  # Retorna o símbolo vencedor

        # Verifica diagonais
        if self.mat[0][0] == self.mat[1][1] == self.mat[2][2] != " ":
            return self.mat[0][0]  # Retorna o símbolo vencedor
        if self.mat[0][2] == self.mat[1][1] == self.mat[2][0] != " ":
            return self.mat[0][2]  # Retorna o símbolo vencedor

        if self.isFull(): #Verifica se o tabuleiro está cheio para dar empate
            return "Empate"

        return None  # Nenhum vencedor ainda




class Player:
    def __init__(self, symbol):
        self.symbol = symbol  # Símbolo do jogador ('X' ou 'O')

    def get_symbol(self):
        return self.symbol
