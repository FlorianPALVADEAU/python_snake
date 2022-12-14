import pygame

class Fruit:
    def __init__(self, snake_info, center):
        self.fruit = snake_info
        self.fruit.center = center
        
        
    def Draw(self, screen, color, info):
        pygame.draw.rect(screen, color, info)
        