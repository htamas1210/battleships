import pygame
import sys
from constants import *

def main():
    print("Starting BattleShip!")

    pygame.init()

    if pygame.get_init() == False:
        pygame.quit()
        sys.exit(1)

    print("Please input your list of positions, from smallest ship to the largest, for your ships.")
    print("Format: a[A]1-a[A]5 b[B]2-b[B]3. [A] means it can either be upper or lower case.")
    print("You need to place five ships with sizes: 5, 4, 3, 3, 2. Otherwise the game won't start")
    print("Have fun")
    
    good_inp = False
    player_board = []
    enemy_board = []
    while good_inp == False:
        inp = input()
        good_inp, player_board = check_valid_input(inp)
        enemy_board = player_board.copy()


    for i in range(10):
        for j in range(10):
            print(f"{board[i][j]} ", end="")
        print()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting Battleships")
                return

        pygame.Surface.fill(screen, (0,0,0))

        

        pygame.display.flip() #refresh screen



        dt = time.tick(60) / 1000 #converted to ms


def check_valid_input(inp):
    s = inp.split(' ')
    print("s", s)
    board = []
    for i in range(10):
        board.append([])
        for _ in range(10):
            board[i].append(0)

    if len(s) != 5:
        print("Not valid input. Please input again")
        return (False, board)
    else:
        for position in s:
            position = position.lower()
            t = position.split("-")
            print("t", t)

            if t[0][0] == t[1][0] and ord(t[0][0]) >= 97 and ord(t[0][0]) <= 107 and ord(t[1][0]) >= 97 and ord(t[1][0]) <= 107: #check if the fist chars match
                if int(t[0][1]) >= 0 and int(t[0][1]) <= 9 and int(t[1][1]) >= 0 and int(t[1][1]) <= 9 and int(t[0][1]) != int(t[1][1]) and abs(int(t[0][1]) - int(t[1][1]))+1 < 6: #check if number is in correct range
                    if int(t[0][1]) > int(t[1][1]):
                        step = -1
                    else:
                        step = 1
                    
                    print(int(t[0][1]), int(t[1][1]))
                    for column in range(int(t[0][1]), int(t[1][1])+1, step):
                        if board[ord(t[0][0])-97][column] == 0b01:
                            print("this position is already taken!")
                            return (False, board)

                        print("in")
                        board[ord(t[0][0])-97][column] = 0b01 #first means if it is hit, second means placement
                        
                    print(board)
                else:
                    print("e1")
                    return (False, board)
            elif t[0][1] == t[1][1] and int(t[0][1]) <= 9 and int(t[1][1]) >= 0 and int(t[1][1]) <= 9 and abs(int(t[0][1]) - int(t[1][1]))+1 < 6:
                print("in2")
                if ord(t[0][0]) >= 97 and ord(t[0][0]) <= 107 and ord(t[1][0]) >= 97 and ord(t[1][0]) <= 107 and t[0][0] != t[1][0]:
                    if ord(t[0][0]) > ord(t[1][0]):
                        step = -1
                    else:
                        step = 1
                    
                    for row in range(ord(t[0][0])-97, ord(t[1][0])-97+1, step):
                        if board[row][int(t[0][1])] == 0b01:
                           print("this position is already taken!")
                           return (False, board)

                        print("in3")
                        board[row][int(t[0][1])] = 0b01 #first means if it is hit, second means placement
                        
                    print(board)
            else:
                print("e2")
                return (False, board)

    print("e3")
    return (True, board)



if __name__ == "__main__":
    main()
