class Player():
    def __init__(self, board, ships = 5):
        self.board = board
        self.ships = ships #alive ships
        self.shot_positions = [] #just add the shot positions here individually

    def get_hit(self, position):
        pass

    def shoot(self, position):
        pass

