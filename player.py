import pygame
from pygame import Rect
class Player():
    def __init__(self, board, ships = 5):
        self.board = board
        self.ships = ships #alive ships
        self.shot_positions = []
        for i in range(0, len(board)):
            self.shot_positions.append([])
            for j in range(0, len(board[0])):
                self.shot_positions[i].append(0)
                #self.shot_positions[i][j] = 0b01

    def get_hit(self, position):
        pass

    def shoot(self, position):
        pass

    def __check_valid_input(self, position):
        if len(position) != 2 and position != None:
            return False

        if ord(position[0]) >= 97 and ord(position[0]) <= 107 and int(position[1]) <= 9 and int(position[1]) >= 0:
            return True

        return False



    def update(self, enemy_board):
        inp = input("Please input the position you want to fire.")
        while self.__check_valid_input(inp) == False:
            inp = input("Please input the position you want to fire.")
            
        self.shoot(inp)

    def draw(self, screen):
        start_pos_x = 125
        start_pos_y = 30
        width = 80
        height = 50

        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                pygame.draw.rect(screen, (0,0,0), Rect(start_pos_x, start_pos_y, width, height), 5)

                if self.shot_positions[i][j] == 0b01:
                    pygame.draw.circle(screen, (0,255,0), (start_pos_x+width//2, start_pos_y + height // 2), 20)
                elif self.shot_positions[i][j] == 0b11:
                    pygame.draw.circle(screen, (255,0,0), (start_pos_x+width//2, start_pos_y + height // 2), 20)
    
                start_pos_x += width - 5

            start_pos_y += height - 5
            start_pos_x = 125
        
        start_pos_y += 50

        #player ship board
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                pygame.draw.rect(screen, (0,0,0), Rect(start_pos_x, start_pos_y, width, height), 5)

                if self.board[i][j] == 0b01:
                    pygame.draw.circle(screen, (255,255,0), (start_pos_x+width//2, start_pos_y + height // 2), 20)
                elif self.board[i][j] == 0b11:
                    pygame.draw.circle(screen, (255,0,0), (start_pos_x+width//2, start_pos_y + height // 2), 20)

                start_pos_x += width - 5

            start_pos_y += height - 5
            start_pos_x = 125

