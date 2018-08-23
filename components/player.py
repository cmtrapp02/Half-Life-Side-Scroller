import pygame
from pygame import *

import constants


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
                    #print(sp)
                    if self.rect.right <= sp.rect.left + 10:
                        RIGHT = constants.Playercollision.RIGHT
                        #print('sp.right')
                    if self.rect.left >= sp.rect.right - 10:
                        LEFT = constants.Playercollision.LEFT
                        #print('sp.left')
                    if self.rect.bottom <= sp.rect.top + 10:
                        BOTTOM = constants.Playercollision.BOTTOM
                        #print('sp.bottom')
                    if self.rect.top >= sp.rect.bottom - 10:
                        TOP = constants.Playercollision.TOP
        
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
            if self.collision_offset[1] == constants.Playercollision.LEFT:
                self.direction = 0
        if pressed[K_d]:
            self.direction += 1
            if self.collision_offset[0] == constants.Playercollision.RIGHT:
                #print('right')
                self.direction = 0
        if pressed[K_w]:
            self.pos_y += -1
            if self.collision_offset[3] == constants.Playercollision.TOP:
                self.pos_y = 0
        self.pos_y += constants.Game.GRAVITY #apply gravity
        if self.collision_offset[2] == constants.Playercollision.BOTTOM:
            self.pos_y = 0
        self.move_ip = self.rect.move_ip(self.direction * self.speed, self.pos_y * self.speed)
