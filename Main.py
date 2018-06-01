import pygame, os.path
from pygame.locals import *

import Constants
import Images

#draw the screen surface
def draw_surface():

    screen_width = 1600
    screen_height = 1400
    surface = pygame.display.set_mode((screen_width, screen_height))
    surface.fill(Constants.colors.WHITE)

    return screen_width, screen_height, surface


#player class
class Player(pygame.sprite.Sprite):
    
    #initialize the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
            
    
    #move player rect
    def move_player(self, x, y):
        
        _, _, surface = draw_surface()
        self.player_image = pygame.image.load('Data/testplayer.png')
        self.player_rect = self.player_image.get_rect(topleft=(x, y))
        self.move_player = surface.blit(self.player_image,self.player_rect)
        
        return self.move_player

        
 #main function for calling other functions       
def main():
    #initialize pygame
    pygame.init()

    #initialize display variables
    width, height, surface = draw_surface()
    pos_x = width / 3
    pos_y = 0

    #load the player image
    #image = pygame.image.load('Data/cat.png') ***

    #initialize clock variables
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

        #apply gravity
        gravity = Constants.game.GRAVITY
        pos_y += gravity

        #move the player
        player.move_player(pos_x, pos_y)

        #draw the scene
        dirty = all.draw(surface)
        pygame.display.update()

        #output the fps to the commandline
        display_fps = clock.get_fps()
        print(display_fps)

        #sprite test code

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(40)
        
        

    pygame.time.wait(1000)

main()