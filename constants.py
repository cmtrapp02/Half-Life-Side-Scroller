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
    SPEED = 3
    JUMP = 0
    SCREENRECT = Rect(0, 0, 600, 400)


class Playercollision(Enum):

    TOP = 100
    BOTTOM = 200
    LEFT = 300
    RIGHT = 400       
    OVERLAP_TOP = 500
    OVERLAP_BOTTOM = 600
    OVERLAP_LEFT = 700
    OVERLAP_RIGHT = 800  