import pygame
from pygame import Rect
from ship import *

class Player():
    def __init__(self, board, ships):
        self.board = board
        self.shot_positions = []
        for i in range(0, len(board)):
            self.shot_positions.append([])
            for _ in range(0, len(board[0])):
                self.shot_positions[i].append(0)
        
        self.ships = []
        for ship in ships: #[(start, end), (start, end)
            self.ships.append(Ship(ship[0], ship[1]))

    def get_hit(self, position):
        self.board[ord(position[0])-97][int(position[1])] = 0b11

    def shoot(self, position, enemy):
        print("p", position)
        
        if enemy.board[ord(position[0])-97][int(position[1])] == 0b00:
            print("No ship at this position")
        else:
            enemy.get_hit(position)
            self.shot_positions[ord(position[0])-97][int(position[1])] = 0b11

    def __check_valid_input(self, position):
        if len(position) != 2 and position != None:
            return False

        if ord(position[0]) >= 97 and ord(position[0]) <= 107 and int(position[1]) <= 9 and int(position[1]) >= 0:
            return True

        if self.shot_positions[ord(position[0])-97][int(position[1])] == 0b11:
            print("You already shot at this position!")
            return False

        return False

    def update(self, enemy):
        inp = input("Please input the position you want to fire.")
        while self.__check_valid_input(inp) == False:
            inp = input("Please input the position you want to fire.")

        self.shoot(inp, enemy)

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

