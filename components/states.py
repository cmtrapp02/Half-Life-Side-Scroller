import pygame
from pygame import *


def is_colliding(sprite, group):
    """returns true if the target sprite is colliding with another in a group, false if not"""
    
    mask = pygame.sprite.collide_mask
    collide = pygame.sprite.spritecollide(sprite, group, False, mask)
    if collide:
        return True
    else:
        return False


def colliding_right(sprite1, sprite2):
    """returns true if the target sprite is colliding on the right with another, false if not"""

    if sprite1.rect.right == sprite2.rect.left + 3:
        return True
    else:
        return False


def colliding_left(sprite1, sprite2):
    """returns true if the target sprite is colliding on the left with another, false if not"""

    if sprite1.rect.left >= sprite2.rect.right - 3:
        return True
    else:
        return False


def colliding_bottom(sprite1, sprite2):
    """returns true if the target sprite is colliding on the bottom with another, false if not"""

    if sprite1.rect.bottom <= sprite2.rect.top + 3:
        return True
    else:
        return False


def colliding_top(sprite1, sprite2):
    """returns true if the target sprite is colliding on the top with another, false if not"""

    if sprite1.rect.top >= sprite2.rect.bottom - 3:
        return True
    else:
        return False


def overlaping_right(sprite1, sprite2):
    """detects if the right side of the targe sprite is inside another, returns true if so,
    false if not"""
   
    if sprite1.rect.right <= sprite2.rect.left + 10:
        return True
    else:
        return False


def overlaping_left(sprite1, sprite2):
    """detects if the left side of the target sprite is inside another, returns true if so, 
    false if not"""

    if sprite1.rect.left >= sprite2.rect.right - 10:
        return True
    else:
        return False

    
def overlaping_top(sprite1, sprite2):
    """detects if the top side of the target sprite is inside another, returns true if so, 
    false if not"""

    if sprite1.rect.top >= sprite2.rect.bottom + 10:
        return True
    else:
        return False


def overlaping_bottom(sprite1, sprite2):
    """detects if the bottom side of the target sprite is inside another, return true if so, 
    false if not"""

    if sprite1.rect.bottom <= sprite2.rect.top + 10:
        return True
    else:
        return False


def is_moving(x, y):
    """returns true if the target sprite is moving, false if not"""

    if x != 0 or y != 0:
        return True
    else:
        return False


def is_grounded(sprite1, sprite2):
    """returns true if the target sprite is on the ground, false if not"""

    if colliding_bottom(sprite1, sprite2):
        return True
    else:
        return False


def is_jumping(jump):
    """returns true if the target sprite is jumping, false if not"""

    if jump == -1:
        return True
    else:
        return False


def facing_left():
    """returns true if the player is facing left, false if not"""
    


def facing_right():
    """returns true if the player is facing right, false if not"""

    