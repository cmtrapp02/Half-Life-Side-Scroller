import pygame, os.path
from pygame.locals import *

import Constants

#draw the screen surface
def draw_screen():

    screen_width = 1680
    screen_height = 1050
    screen = pygame.display.set_mode((screen_width, screen_height))

    return screen_width, screen_height, screen


#player class
class Player():
    

    #initialize player rect
    def __init__(self):
        
        #initalize the size and location of a rectangle
        self.rect = pygame.Rect(0, 0 , 50, 75)
        
        
    #move player rect
    def move_player(self, x, y):
        
        #def player_move(x, y):
        _, _, surface = draw_screen()
        self.move_rect = self.rect.move(x, y)
        self.draw_rect = pygame.draw.rect(surface, Constants.Colors.ORANGE, self.move_rect) #draw the rectangle on the screen
        
    
 #main function for calling other functions       
def main():
    #initialize pygame
    pygame.init()

    #initialize display variables
    width, height, screen = draw_screen()
    pos_x = width / 3
    pos_y = height / 2


    clock = pygame.time.Clock()
    player = Player()


    all = pygame.sprite.RenderUpdates()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        #keyboard inputs
        pressed = pygame.key.get_pressed()
        if pressed[K_a]:
            pos_x += -10
        if pressed[K_d]:
            pos_x += 10

        #move the player
        player.move_player(pos_x, pos_y)

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        #output the fps to the commandline
        fps = clock.get_fps()
        print(fps)

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(40)
        
        

    pygame.time.wait(1000)

main()