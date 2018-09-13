import pygame
from pygame import *

import constants


def is_colliding(sprite, group):
    """
    detects if the target sprite is colliding with another within a given group. Uses
    masks as a callback for more accuracy

    Args:
        sprite: target sprite used to detect if it is colliding
        group: a container that holds sprites to collide against player

    Returns:
        returns true if the player is colliding with another sprite in the group,
        false if not
    """
    
    mask = pygame.sprite.collide_mask
    collide = pygame.sprite.spritecollide(sprite, group, False, mask)
    if collide:
        return True
    else:
        return False


def colliding_right(sprite1, sprite2):
    """
    detects if the target sprite is colliding with another. If so, it then proceeds to 
    judge whether or not the right side of the target is equal to the left side of the 
    colliding sprite within a margin of 3
    
    Args:
        sprite1: the target sprite, collision detects the right side of this sprite
        sprite:2: the colliding sprite, collision detects the left side of this sprite

    Returns:
        returns true if target sprite is colliding on the right, false if not
    """

    if pygame.sprite.collide_rect(sprite1, sprite2):
        if sprite1.rect.right == sprite2.rect.left + 3:
            return True
        else:
            return False


def colliding_left(sprite1, sprite2):
    """
    detects if the target sprite is colliding with another. If so, it then proceeds to 
    judge whether or not the left side of the target is equal to the right side of the
    colliding sprite within a margin of 3
    
    Args:
        sprite1: the target sprite, collision detecst the left side of this sprite
        sprite:2: the colliding sprite, collision detects the right side of this sprite

    Returns:
        returns true if target sprite is colliding on the left, false if not
    """

    if pygame.sprite.collide_rect(sprite1, sprite2):
        if sprite1.rect.left >= sprite2.rect.right - 3:
            return True
        else:
            return False


def colliding_bottom(sprite1, sprite2):
    """
    detects if the target sprite is colliding with another. If so, it then proceeds to 
    judge whether or not the bottom side of the target is equal to the top side of the
    colliding sprite within a margin of 3
    
    Args:
        sprite1: the target sprite, collision detecst the bottom side of this sprite
        sprite:2: the colliding sprite, collision detects the top side of this sprite

    Returns:
        returns true if target sprite is colliding on the bottom, false if not
    """

    if pygame.sprite.collide_rect(sprite1, sprite2):
        if sprite1.rect.bottom <= sprite2.rect.top + 3:
            return True
        else:
            return False


def colliding_top(sprite1, sprite2):
    """
    detects if the target sprite is colliding with another. If so, it then proceeds to 
    judge whether or not the top side of the target is equal to the bottom side of the
    colliding sprite within a margin of 3
    
    Args:
        sprite1: the target sprite, collision detects the top side of this sprite
        sprite:2: the colliding sprite, collision detects the bottom side of this sprite

    Returns:
        returns true if target sprite is colliding on the top, false if not
    """

    if pygame.sprite.collide_rect(sprite1, sprite2):
        if sprite1.rect.top >= sprite2.rect.bottom - 3:
            return True
        else:
            return False


def overlaping_right(sprite1, sprite2):
    """detects if the right side of the targe sprite is inside another, returns true if so,
    false if not"""
   
    if pygame.sprite.collide_rect(sprite1, sprite2):
        if sprite1.rect.right <= sprite2.rect.left + 10:
            return True
        else:
            return False


def overlaping_left(sprite1, sprite2):
    """detects if the left side of the target sprite is inside another, returns true if so, 
    false if not"""

    if pygame.sprite.collide_rect(sprite1, sprite2):
        if sprite1.rect.left >= sprite2.rect.right - 10:
            return True
        else:
            return False

    
def overlaping_top(sprite1, sprite2):
    """detects if the top side of the target sprite is inside another, returns true if so, 
    false if not"""
    
    if pygame.sprite.collide_rect(sprite1, sprite2):
        if sprite1.rect.top >= sprite2.rect.bottom + 10:
            return True
        else:
            return False


def overlaping_bottom(sprite1, sprite2):
    """detects if the bottom side of the target sprite is inside another, return true if so, 
    false if not"""

    if pygame.sprite.collide_rect(sprite1, sprite2):
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
    elif overlaping_bottom(sprite1, sprite2):
        return True
    else:
        return False


def can_jump(pos):

    if pos == 0:
        return True
    else:
        return False


def is_jumping(jump):
    """returns true if the target sprite is jumping, false if not"""

    if jump >= 1:
        return True
    else:
        return False


def is_falling(pos):
    """
    """


def facing_left():
    """returns true if the player is facing left, false if not"""
    


def facing_right():
    """returns true if the player is facing right, false if not"""

    