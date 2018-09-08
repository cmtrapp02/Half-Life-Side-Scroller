import pygame
from pygame import *

import constants
import states

class Player(pygame.sprite.Sprite):

    #initialize the player
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = constants.Game.SPEED
        self.gravity = constants.Game.GRAVITY
        self.vel = ([5,5])
        self.i = img
        self.image = pygame.image.load(self.i)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.facing = 1
        self.sp = []

    #handle collisions
    def collide(self, group, sprites, index):
        """Detect which sides are colliding"""

        self.collision_offset = [0, 0, 0, 0]
        RIGHT = 0
        LEFT = 0
        BOTTOM = 0 
        TOP = 0
        if states.is_colliding(self, group):
            for index in range(len(sprites)):
                self.sp = sprites[index]
                rect_collide = pygame.sprite.collide_rect(self, self.sp)
                if rect_collide:
                    if states.colliding_right(self, self.sp):
                        RIGHT = constants.Playercollision.RIGHT
                    elif states.overlaping_right(self, self.sp):
                        RIGHT = constants.Playercollision.OVERLAP_RIGHT

                    if states.colliding_left(self, self.sp):
                        LEFT = constants.Playercollision.LEFT
                    elif states.overlaping_left(self, self.sp):
                        LEFT = constants.Playercollision.OVERLAP_LEFT

                    if states.colliding_bottom(self, self.sp):
                        BOTTOM = constants.Playercollision.BOTTOM
                    elif states.overlaping_bottom(self, self.sp):
                        BOTTOM = constants.Playercollision.OVERLAP_BOTTOM

                    if states.colliding_top(self, self.sp):
                        TOP = constants.Playercollision.TOP
                    elif states.overlaping_top(self, self.sp):
                        TOP = constants.Playercollision.OVERLAP_TOP

                    self.collision_offset = [RIGHT, LEFT, BOTTOM, TOP]
                    index += 1    

    #move the player
    def move(self):
        self.direction = 0
        self.facing = self.direction
        pressed = pygame.key.get_pressed()
        self.pos_y = 0
        self.jumping = False
        if pressed[K_a]:
            self.direction += -1
            if self.collision_offset[1] == constants.Playercollision.LEFT: #TODO for all 4, rethink how state machine can be implemented for this
                self.direction = 0
            elif self.collision_offset[1] == constants.Playercollision.OVERLAP_LEFT:
                self.direction += 1

        if pressed[K_d]:
            self.direction += 1
            if self.collision_offset[0] == constants.Playercollision.RIGHT: #TODO
                self.direction = 0
            elif self.collision_offset[0] == constants.Playercollision.OVERLAP_RIGHT:
                self.direction += -1

        if self.collision_offset[2] == constants.Playercollision.BOTTOM and not self.jumping:
            self.pos_y = 0
        elif self.collision_offset[2] == constants.Playercollision.OVERLAP_BOTTOM:
            self.pos_y = -1
        elif not states.is_jumping(self.pos_y):
            self.pos_y += constants.Game.GRAVITY

        self.move_ip = self.rect.move_ip(self.direction * self.speed, self.pos_y * self.speed) #TODO: change the values of speed for the y axis based upon when the player is jumping or falling
