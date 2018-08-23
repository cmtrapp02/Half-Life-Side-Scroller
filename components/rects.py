import pygame
from pygame import *

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