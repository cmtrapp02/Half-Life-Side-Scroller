import os.path
import sys
import pygame
from pygame import *

sys.path.insert(0, 'components')
sys.path.insert(0, 'graphics')

from player import Player
from rects import Rects
import states

#initialize classes and other variables
class Level1():

    def __init__(self):

        #game images
        player_image = 'graphics/testplayer.png'
        rect_image = 'graphics/bluetestrect.png'
        rect_image2 = 'graphics/cat.png'
        blue_image = 'graphics/glaucousbluerect.png'
        box_image = 'graphics/testbox.png'
        background_image = 'graphics/testbackground.png'
        ground_image = 'graphics/testrectground.png'
    
        #initialize game classes
        self.player = Player(player_image)
        self.test_rect = Rects(rect_image)
        self.test_rect2 = Rects(rect_image2)
        self.test_rect3 = Rects(blue_image)
        self.blue_sprite1 = Rects(blue_image)
        self.blue_sprite2 = Rects(blue_image)
        self.blue_sprite3 = Rects(blue_image)
        self.blue_sprite4 = Rects(blue_image)
        self.test_box = Rects(box_image)
        self.test_background = Rects(background_image)
        self.test_ground = Rects(ground_image)

        #update the rect locations
        self.test_rect.update(0, 225)
        self.test_rect2.update(300, 225)
        self.test_rect3.update(200, 100)
        self.test_box.update(0, 0)
        self.test_background.update(0, 0)
        self.test_ground.update(0, 350)
        self.blue_sprite1.update(0, 250)
        self.blue_sprite2.update(400, 250)
        self.blue_sprite3.update(400, 0)
        self.blue_sprite4.update(600, 350)


        #sprite groups
        self.sprites = [self.test_ground, self.blue_sprite1, self.blue_sprite2]
        self.player_group = pygame.sprite.Group(self.player)
        self.blocking_group = pygame.sprite.Group(self.sprites)
        self.background_group = pygame.sprite.Group(self.test_background)

        #used to get the index of a list
        self.index = 0

        self.all = pygame.sprite.RenderUpdates(self.background_group, self.blocking_group, self.player_group)

    def update(self, surface, clock):
        
        #handle player inputs and collision
        s = surface
        c = clock

        self.player.collide(self.blocking_group, self.sprites, self.index)
        self.player.move()

        #draw the scene
        dirty = self.all.draw(s)
        #if states.overlaping_bottom(self.player, self.sprites[self.index]):
        #else:
        pygame.display.update(dirty)

        #output the fps to the commandline
        display_fps = c.get_fps()
        #print(display_fps)

        #TODO: fix timestep
        #Cap the frame rate at 60 TEMPORARY
        c.tick(60)