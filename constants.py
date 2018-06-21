import pygame
from pygame.locals import *

#game constants

class colors:

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    ORANGE = (255,165,0)


class game:

    GRAVITY = 9.8
    SCREENRECT = Rect(0, 0, 600, 400)