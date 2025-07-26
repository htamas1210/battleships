import pygame
import sys
from constants import *
from player import *

def main():
    print("Starting BattleShip!")

    pygame.init()

    if pygame.get_init() == False:
        pygame.quit()
        sys.exit(1)

    print("Please input your list of positions, from smallest ship to the largest, for your ships.")
    print("Format: a[A]1-a[A]5 b[B]2-b[B]3. [A] means it can either be upper or lower case. Please input the positions from lowest to highest.")
    print("You must have 5 ships. The ships can be of any size between 1 and 5.")
    print("Have fun.")
    
    good_inp = False
    player_board = []
    enemy_board = []
    while good_inp == False:
        inp = input()
        good_inp, player_board = check_valid_input(inp)
        enemy_board = player_board.copy()

    player = Player(player_board)
    enemy = Player(enemy_board)

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(f"{player.board[i][j]} ", end="")
        print()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()
    dt = 0
    first_iteration = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting Battleships")
                return

        pygame.Surface.fill(screen, (255,255,255))
        
        if first_iteration == False:
            player.update(enemy_board)
        else:
            first_iteration = False

        player.draw(screen)

        pygame.display.flip() #refresh screen

        dt = time.tick(60) / 1000 #converted to ms


def check_valid_input(inp):
    s = inp.split(' ')
    print("s", s)
    board = []
    for i in range(BOARD_SIZE):
        board.append([])
        for _ in range(BOARD_SIZE):
            board[i].append(0)

    if len(s) != 5:
        print("Not valid input. Please input again")
        return (False, board)
    else:
        count = 0
        for position in s:
            count += 1
            print("c", count)
            position = position.lower()
            t = position.split("-")
            print("t", t)

            if t[0][0] == t[1][0] and ord(t[0][0]) >= 97 and ord(t[0][0]) <= 107 and ord(t[1][0]) >= 97 and ord(t[1][0]) <= 107: #check if the fist chars match
                if int(t[0][1]) >= 0 and int(t[0][1]) <= 9 and int(t[1][1]) >= 0 and int(t[1][1]) <= 9 and int(t[0][1]) != int(t[1][1]) and abs(int(t[0][1]) - int(t[1][1]))+1 < 6: #check if number is in correct range
                    if int(t[0][1]) > int(t[1][1]):
                        step = -1
                    else:
                        step = 1
                    
                    for column in range(int(t[0][1]), int(t[1][1])+1, step):
                        if board[ord(t[0][0])-97][column] == 0b01:
                            print("this position is already taken!")
                            return (False, board)

                        board[ord(t[0][0])-97][column] = 0b01 #first means if it is hit, second means placement
                        
                        for i in range(BOARD_SIZE):
                            for j in range(BOARD_SIZE):
                                print(f"{board[i][j]} ", end="")
                            print()
                else:
                    print("e1")
                    return (False, board)
            elif t[0][1] == t[1][1] and int(t[0][1]) <= 9 and int(t[1][1]) >= 0 and int(t[1][1]) <= 9 and abs(int(t[0][1]) - int(t[1][1]))+1 < 6:
                if ord(t[0][0]) >= 97 and ord(t[0][0]) <= 107 and ord(t[1][0]) >= 97 and ord(t[1][0]) <= 107 and t[0][0] != t[1][0]:
                    if ord(t[0][0]) > ord(t[1][0]):
                        step = -1
                    else:
                        step = 1
                    
                    for row in range(ord(t[0][0])-97, ord(t[1][0])-97+1, step):
                        if board[row][int(t[0][1])] == 0b01:
                           print("this position is already taken!")
                           return (False, board)

                        board[row][int(t[0][1])] = 0b01 #first means if it is hit, second means placement
                        
                    for i in range(BOARD_SIZE):
                        for j in range(BOARD_SIZE):
                            print(f"{board[i][j]} ", end="")
                        print()
            else:
                print("e2")
                return (False, board)

    print("e3")
    return (True, board)



if __name__ == "__main__":
    main()
