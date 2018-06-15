import pygame, os.path
from pygame.locals import *

import Constants

#draw the screen surface
def draw_surface():

    screen_width = 1600
    screen_height = 1400
    surface = pygame.display.set_mode((screen_width, screen_height))

    return screen_width, screen_height, surface

#player class
class Player(pygame.sprite.Sprite):
    
    #initialize the player
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect()

    #move the player
    def move_player(self, x, y):
        
        _, _,surface = draw_surface()
        self.rect.x = x
        self.rect.y = y
        #surface.blit(self.image, self.rect)
        
        
class Rects(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect()


    def update(self, x, y):

        _, _, surface = draw_surface()
        self.rect.x = x
        self.rect.y = y

 #main function for calling other functions       
def main():
    #initialize pygame
    pygame.init()

    #initialize display variables
    width, height, surface = draw_surface()
    pos_x = 0
    pos_y = 0
    fill_screen = surface.fill(Constants.colors.BLUE)

    #initialize clock variables
    clock = pygame.time.Clock()

    #game images
    player_image = 'Data/testplayer.png'
    rect_image = 'Data/testrect.png'
    background_image = 'Data/testbackground.png'
    
    #initialize game classes
    player = Player(player_image)
    test_rect = Rects(rect_image)
    test_background = Rects(background_image)

    #update the rect locations
    test_rect.update(100, 0)
    test_background.update(pos_x / 2, pos_y / 2)

    #sprite groups
    player_group = pygame.sprite.Group(player)
    blocking_group = pygame.sprite.Group(test_rect)
    background_group = pygame.sprite.Group(test_background)

    #sprite layers
    layer_player = pygame.sprite.LayeredUpdates().get_layer_of_sprite(player)
    layer_rect = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_rect)
    layer_background = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_background)

    print('player layer: ' + str(layer_player))
    print('rect layer: ' + str(layer_rect))
    print('layer_background: ' + str(layer_background))

    #pygame.sprite.LayeredUpdates().move_to_front(player)
    
    all = pygame.sprite.RenderUpdates(background_group, blocking_group, player_group)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #clear all sprites
        #all.clear(surface, background_image)
    
        #update all sprites
        #all.update()

        #keyboard inputs
        pressed = pygame.key.get_pressed()
        if pressed[K_a]:
            pos_x += -10
        if pressed[K_d]:
            pos_x += 10

        #detect collisions
        sprite_collide = pygame.sprite.groupcollide(player_group, blocking_group, False, False)
        
        for block in sprite_collide:
            print("Collision Detected!")

        #TODO: apply gravity
        #gravity = Constants.game.GRAVITY
        #pos_y += gravity
        
        #load the player image and move the player
        player.move_player(pos_x, pos_y)
        
        #load rects and their 
        

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