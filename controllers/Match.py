from controllers.Board import Board, OutOfBoundsError, CellOccupiedError

class Match:
    def __init__(self):
        self.board = Board()
        self.winner = None
        self.game_over = False
