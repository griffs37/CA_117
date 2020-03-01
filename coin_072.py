#!usr/bin/env python

from random import randint

class Coin:

    def __init__(self, side='Heads'):
        self.sideup = side

    def flip(self):
        if randint(0,1) == 0:
            self.sideup = 'Tails'
        else:
            self.sideup = 'Heads'

    def getstate(self):
        return self.sideup

    def __str__(self):
        return "Current state : {}".format(self.sideup)
