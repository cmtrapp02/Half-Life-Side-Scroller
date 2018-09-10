# This file contains all the useful little functions that have no where else to go

import pygame
from pygame import *

import timeit

def timer(direction, time):
    """ 
    Set a timer counting up or down using a given number

    Args:
        direction: determins the direction the timer counts
        time: determins the time the timer will be counting to or from

    Returns:
        Returns the time the timer is currently at
    """
