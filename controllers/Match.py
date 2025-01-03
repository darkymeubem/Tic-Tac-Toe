from controllers.Board import Board

class Match:
    def __init__(self):
        self.board = Board(3)
        self.winner = None  # Inicializa o vencedor como None