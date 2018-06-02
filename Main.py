import pygame, os.path
from pygame.locals import *

import Constants

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
        
        #TODO: Make this an argument to call in main rather than in the constructor
        self.player_image = pygame.image.load('Data/testplayer.png')
        self.player_rect = self.player_image.get_rect()
        self._, self._, self.surface = draw_surface()
        

    #move the player
    def move_player(self, x, y):
        
        self.player_rect.x = x
        self.player_rect.y = y
        self.surface.blit(self.player_image, self.player_rect)
        
        
 #main function for calling other functions       
def main():
    #initialize pygame
    pygame.init()

    #initialize display variables
    width, height, surface = draw_surface()
    pos_x = width / 3
    pos_y = 0

    #initialize clock variables
    clock = pygame.time.Clock()

    #initialize the player
    player = Player()

    #load player image
    #player.__init__('Data/testplayer.png')
    

    all = pygame.sprite.RenderUpdates()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #TEMPORARY: test rect for collision
        pygame.draw.rect(surface, Constants.colors.GREEN, (100, 100, 200, 50))

        #keyboard inputs
        pressed = pygame.key.get_pressed()
        if pressed[K_a]:
            pos_x += -10
        if pressed[K_d]:
            pos_x += 10

        #detect collisions
        

        #apply gravity
        #gravity = Constants.game.GRAVITY
        #pos_y += gravity

        #move the player
        player.move_player(pos_x, pos_y)

        #draw the scene
        dirty = all.draw(surface)
        pygame.display.update()

        #output the fps to the commandline
        display_fps = clock.get_fps()
        print(display_fps)

        #
        

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(40)
        
        

    pygame.time.wait(1000)

main()