import pygame, os.path
from pygame.locals import *

def main():

    pygame.init()
    
    screen = pygame.display.set_mode((1680, 1050))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


main()