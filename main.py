import pygame
import sys
from constants import *

def main():
    print("Starting BattleShip!")

    pygame.init()

    if pygame.get_init() == False:
        pygame.quit()
        sys.exit(1)

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

if __name__ == "__main__":
    main()
