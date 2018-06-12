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
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        #TODO: Make this an argument to call in main rather than in the constructor
        self.image = pygame.image.load('Data/testplayer.png')
        self.rect = self.image.get_rect()
        
    #move the player
    def move_player(self, x, y):
        _, _,surface = draw_surface()
        self.rect.x = x
        self.rect.y = y
        #surface.blit(self.image, self.rect)
        
        
class Rects(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.image.load('Data/testrect.png')
        self.rect = self.image.get_rect()

    def update(self, pos_x, pos_y):

        _, _, surface = draw_surface()
        self.rect.x = pos_x
        self.rect.y = pos_y

 #main function for calling other functions       
def main():
    #initialize pygame
    pygame.init()

    #initialize display variables
    width, height, surface = draw_surface()
    pos_x = 0
    pos_y = 0

    #initialize clock variables
    clock = pygame.time.Clock()

    #initialize game classes
    player = Player()
    test_rect = Rects()
    

    all = pygame.sprite.RenderUpdates()

    #assign default group to each class
    Player.containers = all
    Rects.containers = all

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
        #sprite_collide = pygame.sprite.collide_rect(player.rect, test_rect.rect)
        
        #for block in sprite_collide:
            #print("Collision Detected!")

        #apply gravity
        #gravity = Constants.game.GRAVITY
        #pos_y += gravity

        player.move_player(pos_x, pos_y)
        #move the player

        #object positions
        #test_rect.update(500, 0)
        #group.draw(surface)

        #draw the scene
        dirty = all.draw(surface)
        pygame.display.update(dirty)

        #output the fps to the commandline
        display_fps = clock.get_fps()
        #print(display_fps)

        #
        

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(40)
        
        

    pygame.time.wait(1000)

main()