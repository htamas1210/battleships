import pygame
from pygame import Rect
class Player():
    def __init__(self, board, ships = 5):
        self.board = board
        self.ships = ships #alive ships
        self.shot_positions = [] #just add the shot positions here individually

    def get_hit(self, position):
        pass

    def shoot(self, position):
        pass
    
    def update(self):
        pass

    def draw(self, screen):
        start_pos_x = 125
        start_pos_y = 30

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                pygame.draw.rect(screen, (0,0,0), Rect(start_pos_x, start_pos_y, 80, 80), 5)
                start_pos_x += 75
            start_pos_y += 75
            start_pos_x = 125

