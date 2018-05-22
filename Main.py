import pygame, os.path
from pygame.locals import *

import Constants

#draw the screen surface
def draw_screen():

    pygame.init()
    screen_size = (1680, 1050)
    screen = pygame.display.set_mode(screen_size)

    return screen

#player class
class Player():
    
    #initialize player rect
    def __init__():

        orange = Constants.Colors.ORANGE
        
        draw_rect = pygame.draw.rect(draw_screen(), orange, rect)

        return draw_rect


    #move player rect
    def player_move(x, y):

        rect = pygame.Rect(0, 0, 50, 75).move(x, y)
        

        return rect

 #main function for calling functions       
def main():

    draw_screen()
    player = Player.__init__
    move = Player.player_move

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player()
        move(100, 100)

        pygame.display.update()

main()