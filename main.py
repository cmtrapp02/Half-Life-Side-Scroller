import pygame, os.path
from pygame.locals import *

import constants

#player class
class Player(pygame.sprite.Sprite):
    
    speed = 5
    #initialize the player
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect(midbottom=constants.game.SCREENRECT.midbottom)

    #move the player
    def move_player(self, x, y):
        
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

        self.rect.x = x
        self.rect.y = y

 #main function for calling other functions       
def main(winstyle = 0):
    #initialize pygame
    pygame.init()

    #initialize display variables
    winstyle = 0 # toggle fullscreen
    surface = pygame.display.set_mode(constants.game.SCREENRECT.size, winstyle)
    surface.fill(constants.colors.BLUE)

    #initialize clock variables
    clock = pygame.time.Clock()

    #game images
    player_image = 'Data/testplayer.png'
    rect_image = 'Data/glaucousbluerect.png'
    background_image = 'Data/testbackground.png'
    ground_image = 'Data/testrectground.png'
    
    #initialize game classes
    player = Player(player_image)
    test_rect = Rects(rect_image)
    test_background = Rects(background_image)
    test_ground = Rects(ground_image)

    #initialize movement variables
    pos_x = 0
    pos_y = 0

    #update the rect locations
    test_rect.update(100, 0)
    test_background.update(0, 0)
    test_ground.update(0, 300)

    #sprite groups
    player_group = pygame.sprite.Group(player)
    blocking_group = pygame.sprite.Group(test_rect, test_ground)
    background_group = pygame.sprite.Group(test_background)

    #sprite layers
    layer_player = pygame.sprite.LayeredUpdates().get_layer_of_sprite(player)
    layer_rect = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_rect)
    layer_background = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_background)
    
    all = pygame.sprite.RenderUpdates(background_group, blocking_group, player_group)

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

        #detect collisions
        sprite_collide = pygame.sprite.spritecollideany(player, blocking_group,)
        
        if sprite_collide:
            print("Collision detected")

        #TODO: apply gravity
        #gravity = Constants.game.GRAVITY
        #pos_y += gravity
        
        #load the player image and move the player
        player.move_player(pos_x, pos_y)

        #draw the scene
        dirty = all.draw(surface)
        pygame.display.update(dirty)

        #output the fps to the commandline
        display_fps = clock.get_fps()
        #print(display_fps)

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(40)
        
        

    pygame.time.wait(1000)

main()