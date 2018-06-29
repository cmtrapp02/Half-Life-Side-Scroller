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
        self.mask = get_mask_surface(self.image)
        self.facing = 1

    #move the player
    def move(self, direction):
        
        self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect.top = 225
        
        
class Rects(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, x, y):

        self.rect.x = x
        self.rect.y = y

def get_mask_surface(surface, threshold = 127):

    mask = pygame.mask.from_surface(surface.get_size())

 #main function for calling other functions       
def main(winstyle = 0):
    #initialize pygame
    pygame.init()

    #initialize display variables
    winstyle = 1 # toggle fullscreen
    surface = pygame.display.set_mode(constants.game.SCREENRECT.size, winstyle)
    surface.fill(constants.colors.BLUE)
    pygame.display.flip()

    #initialize clock variables
    clock = pygame.time.Clock()

    #game images
    player_image = 'Data/redtestrect.png'
    rect_image = 'Data/screentestrect.png'
    background_image = 'Data/testbackground.png'
    ground_image = 'Data/testrectground.png'
    
    #initialize game classes
    player = Player(player_image)
    test_rect = Rects(rect_image)
    test_background = Rects(background_image)
    test_ground = Rects(ground_image)

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

    #load the sprite masks for collision
    #x = player.image.get_width()
    #y = player.image.get_height()
    #test_mask = player.mask.get_size()
    #test_mask1 = test_rect.mask.get_size() 


    #TEMPORARY: used for offset within masks
    
    
    all = pygame.sprite.RenderUpdates(background_group, blocking_group, player_group)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #handle player inputs and collision
        pressed = pygame.key.get_pressed()
        #sprite_collide = pygame.sprite.spritecollideany(player, blocking_group)
    
        direction = 0
        if pressed[K_a]:
            direction += -1
        if pressed[K_d]:
            direction += 1
        
        player.move(direction)

        #testing collision mask
        #test_rect.mask.set_at((0, 0))
        #player.mask.set_at((0, 0))

        get_size = player.mask.get_size()
        get_at = player.mask.get_at((0,0))
        set_at = player.mask.set_at((0,0))
        overlap_area = player.mask.overlap_area(test_rect.mask, (25, 12))
        print('get at: ' + str(get_at))
        print('overlapt area: ' + str(overlap_area))

        callback = pygame.sprite.collide_mask(player, test_rect)
        sprite_collide = pygame.sprite.spritecollide(player, blocking_group, False, callback)
        print('callback: ' + str(callback))

        #TODO: apply gravity
        #gravity = Constants.game.GRAVITY
        #pos_y += gravity

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