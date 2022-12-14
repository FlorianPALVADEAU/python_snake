import pygame
from random import randrange

class Screen:
    def __init__(self, mainWindowSize, caption, tileSet, timee, time_step):
        self.screen = pygame.display.set_mode([mainWindowSize] *2)
        self.mainWindowSize = mainWindowSize
        self.caption = pygame.display.set_caption(caption)
        self.tileSet = tileSet
        self.range = (tileSet // 2, mainWindowSize - tileSet //2, tileSet)
        self.get_random_position = lambda: [randrange(*self.range), randrange(*self.range)]
        self.time = timee
        self.time_step = time_step


        