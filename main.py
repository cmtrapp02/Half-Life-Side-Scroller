
import pygame, os.path
import sys
import pygame
from pygame.locals import *

sys.path.insert(0, 'components')

import constants
from player import Player
from rects import Rects
import levels

 #main function for calling other functions       
def main(winstyle = 0):
    #initialize pygame
    pygame.init()

    #initialize display variables #TODO look into possibly moving to main loop
    surface = pygame.display.set_mode(constants.Game.SCREENRECT.size, pygame.SRCALPHA)
    surface.fill(constants.Colors.BLUE)
    pygame.display.flip()

    #initialize clock variables
    clock = pygame.time.Clock()
    lvl1 = levels.Level1()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
                sys.exit()

        #call levels
        test = 0
        lvl1.update(surface, clock)
        

    pygame.time.wait(1000)

main()