import pygame, os.path
from pygame.locals import *

import constants
from constants import Playercollision

#player class
class Player(pygame.sprite.Sprite):
    

    #initialize the player
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = 3
        self.vel = ([5,5])
        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.facing = 1

    #move the player
    def move(self):
        self.direction = 0
        self.facing = self.direction
        pressed = pygame.key.get_pressed()
        self.pos_y = 0
        if pressed[K_a]:
            self.direction += -1
        if pressed[K_d]:
            self.direction += 1
        if pressed[K_w]:
            self.pos_y += -1
        if pressed[K_s]:
            self.pos_y += 1
        self.rect.move_ip(self.direction * self.speed, self.pos_y * self.speed)
        #self.rect.top = 100
        
    def collide(self, blocking_group, offset):

        mask = pygame.sprite.collide_mask
        self.collide = pygame.sprite.spritecollide(self, blocking_group, False, mask)
        if self.direction - offset == 0:
            self.direction = 0

class Rects(pygame.sprite.Sprite):

    def __init__(self, img):
        
        pygame.sprite.Sprite.__init__(self)
        self.test = ([1,1])
        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def update(self, x, y):
        self.x = 0
        self.y = 0
        self.rect.move_ip(self.x, self.y)

 #main function for calling other functions       
def main(winstyle = 0):
    #initialize pygame
    pygame.init()

    #initialize display variables
    winstyle = 1 # toggle fullscreen
    surface = pygame.display.set_mode(constants.Game.SCREENRECT.size, pygame.SRCALPHA)
    surface.fill(constants.Colors.BLUE)
    pygame.display.flip()

    #initialize clock variables
    clock = pygame.time.Clock()

    #game images
    player_image = 'data/testplayer.png'
    rect_image = 'data/bluetestrect.png'
    rect_image2 = 'data/yellowtestrect.png'
    rect_image3 = 'data/glaucousbluerect.png'
    background_image = 'data/testbackground.png'
    ground_image = 'data/testrectground.png'
    
    #initialize game classes
    player = Player(player_image)
    test_rect = Rects(rect_image)
    test_rect2 = Rects(rect_image2)
    test_rect3 = Rects(rect_image3)
    test_background = Rects(background_image)
    test_ground = Rects(ground_image)

    #update the rect locations
    test_rect.update(50, 225)
    test_rect2.update(400, 225)
    test_rect3.update(200, 100)
    test_background.update(0, 0)
    test_ground.update(0, 300)

    #sprite groups
    player_group = pygame.sprite.Group(player)
    blocking_group = pygame.sprite.Group(test_rect, test_rect2, test_rect3)
    background_group = pygame.sprite.Group(test_background)

    #sprite layers
    #layer_player = pygame.sprite.LayeredUpdates().get_layer_of_sprite(player)
    #layer_rect = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_rect)
    #layer_background = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_background)

    print('player rect size: ' + str(player.rect.size))
    print('3rd test rect size: ' + str(test_rect3.rect.size))
    print('player mask size: ' + str(player.mask.get_size()))
    print('3rd test rect mask size: ' + str(test_rect3.mask.get_size()))

    iii = 0

    all = pygame.sprite.RenderUpdates(background_group, blocking_group, player_group)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        get_size = player.mask.get_size()
        get_at = player.mask.get_at((0,0))
        set_at = player.mask.set_at((0,0))
        
        sprites = [test_rect, test_rect2, test_rect3]
        
        #handle player inputs and collision
        player.move()
        player.collide(blocking_group, test_rect3.rect.x)

        #draw the scene
        dirty = all.draw(surface)
        pygame.display.update(dirty)

        #output the fps to the commandline
        display_fps = clock.get_fps()
        #print(display_fps)

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(60)
        
        

    pygame.time.wait(1000)

main()