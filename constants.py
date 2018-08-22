import pygame
from pygame.locals import *
from enum import Enum

#game constants

class Colors:

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    ORANGE = (255,165,0)


class Game:

    GRAVITY = 3
    SCREENRECT = Rect(0, 0, 600, 400)


class Playercollision(Enum):

    TOP = 1
    BOTTOM = -1
    LEFT = 1
    RIGHT = -1         