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

    #handle collisions
    def collide(self, group, sprites, index, index2):

        mask = pygame.sprite.collide_mask
        sprite_collide = pygame.sprite.spritecollide(self, group, False, mask)
        self.collision_offset = [0, 0, 0, 0]
        RIGHT = 0
        LEFT = 0
        BOTTOM = 0 
        TOP = 0
        if sprite_collide:
            for index in range(len(sprites)):
                sp = sprites[index]
                rect_collide = pygame.sprite.collide_rect(self, sp)
                if rect_collide:
                    print(sp)
                    if self.rect.right <= sp.rect.left + 5:
                        RIGHT = Playercollision.RIGHT
                        #print('sp.right')
                    if self.rect.left >= sp.rect.right - 5:
                        LEFT = Playercollision.LEFT
                        #print('sp.left')
                    if self.rect.bottom <= sp.rect.top + 5:
                        BOTTOM = Playercollision.BOTTOM
                        #print('sp.bottom')
                    if self.rect.top >= sp.rect.bottom - 5:
                        TOP = Playercollision.TOP
                        #print('sp.top')
                    for index2 in range(len(sprites)):
                        sp2 = sprites[index2]
                        rect_collide2 = pygame.sprite.collide_rect(self, sp2)
                        if rect_collide2 and index2 != index:
                            print(sp2)
                            if self.rect.right <= sp2.rect.left + 5:
                                RIGHT = Playercollision.RIGHT
                                #print('sp2.right')
                            if self.rect.left >= sp2.rect.right - 5:
                                LEFT = Playercollision.LEFT
                                #print('sp2.left')
                            if self.rect.bottom <= sp2.rect.top + 5:
                                BOTTOM = Playercollision.BOTTOM
                                #print('sp2.bottom')
                            if self.rect.top >= sp2.rect.bottom - 5:
                                TOP = Playercollision.TOP
                                #print('sp2.tops')
                            index2 += 1
                    self.collision_offset = [RIGHT, LEFT, BOTTOM, TOP]
                    index += 1    
                    
    #move the player
    def move(self):
        self.direction = 0
        self.facing = self.direction
        pressed = pygame.key.get_pressed()
        self.pos_y = 0
        if pressed[K_a]:
            self.direction += -1
            if self.collision_offset[1] == Playercollision.LEFT:
                self.direction = 0
        if pressed[K_d]:
            self.direction += 1
            if self.collision_offset[0] == Playercollision.RIGHT:
                #print('right')
                self.direction = 0
        if pressed[K_w]:
            self.pos_y += -1
            if self.collision_offset[3] == Playercollision.TOP:
                self.pos_y = 0
        if pressed[K_s]:
            self.pos_y += 1
            if self.collision_offset[2] == Playercollision.BOTTOM:
                #print('bottom')
                self.pos_y = 0
        self.move_ip = self.rect.move_ip(self.direction * self.speed, self.pos_y * self.speed)

class Rects(pygame.sprite.Sprite):

    def __init__(self, img):
        
        pygame.sprite.Sprite.__init__(self)
        self.test = ([1,1])
        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def update(self, x, y):
    
        self.rect.move_ip(x, y)

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
    rect_image2 = 'data/cat.png'
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
    test_rect3.update(203, 100)
    test_background.update(0, 0)
    test_ground.update(0, 300)

    #sprite groups
    player_group = pygame.sprite.Group(player)
    blocking_group = pygame.sprite.Group(test_rect, test_rect2, test_rect3, test_ground)
    background_group = pygame.sprite.Group(test_background)

    #sprite layers
    #layer_player = pygame.sprite.LayeredUpdates().get_layer_of_sprite(player)
    #layer_rect = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_rect)
    #layer_background = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_background)

    print('player rect size: ' + str(player.rect.size))
    print('3rd test rect size: ' + str(test_rect3.rect.size))
    print('player mask size: ' + str(player.mask.get_size()))
    print('3rd test rect mask size: ' + str(test_rect3.mask.get_size()))

    #used to get the index of a list
    index = 0
    index2 = 0

    all = pygame.sprite.RenderUpdates(background_group, blocking_group, player_group)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
                sys.exit()

        get_size = player.mask.get_size()
        get_at = player.mask.get_at((0,0))
        set_at = player.mask.set_at((0,0))
        
        #handle player inputs and collision
        sprites = [test_rect, test_rect2, test_rect3, test_ground]
        player.collide(blocking_group, sprites, index, index2)
        player.move()

        #draw the scene
        dirty = all.draw(surface)
        pygame.display.update(dirty)
        
        #test pixel array library
        

        #output the fps to the commandline
        display_fps = clock.get_fps()
        #print(display_fps)

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(60)
        
        

    pygame.time.wait(1000)

main()