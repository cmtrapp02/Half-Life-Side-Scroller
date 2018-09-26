# This file contains all the useful little functions that have no where else to go

import pygame
from pygame import *

from threading import Timer
import constants

def timer(t, args):
    """ 
    Set a timer that executes a command once the timer has hit zero

    Args:
        time: determins the time the timer will be counting down from
        arg: executes the given argument once the timer hits zero
    """
    
    time = Timer(t, args)
    time.start()
    return


def make_true(arg):
    """
    Makes in argument true. Used in the jumping action to making jumping
    possible once a timer has ended.

    Args:
        arg: the value that is made to be true
    """
    arg = True
    return arg
