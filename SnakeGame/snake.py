import pygame

class Snake:
    def __init__(self, tileSet, length, direction, center):
        self.snake = pygame.rect.Rect([0, 0, tileSet-2, tileSet-2])
        self.length = length
        self.part = [self.snake]
        self.direction = direction
        self.snake.center = center
        self.movement_possibilities = {pygame.K_z: 1, pygame.K_s: 1, pygame.K_q: 1, pygame.K_d: 1}

        
        
    def Move(self, direct):
        self.direction = (direct[0], direct[1])
        
        
    def Draw(self, screen, snake_part):
        [pygame.draw.rect(screen, 'yellow', part) for part in snake_part]
        
        
    def GetMovement(self, event, tileset):
        if event == pygame.K_z and self.movement_possibilities[pygame.K_z]:
            direction = [0, -tileset]
            self.Move(direction)
            self.movement_possibilities = {pygame.K_z: 1, pygame.K_s: 0, pygame.K_q: 1, pygame.K_d: 1}
            
        if event == pygame.K_s and self.movement_possibilities[pygame.K_s]:
            direction = [0, tileset]
            self.Move(direction)
            self.movement_possibilities = {pygame.K_z: 0, pygame.K_s: 1, pygame.K_q: 1, pygame.K_d: 1}
            
        if event == pygame.K_q and self.movement_possibilities[pygame.K_q]:
            direction = [-tileset, 0]
            self.Move(direction)
            self.movement_possibilities = {pygame.K_z: 1, pygame.K_s: 1, pygame.K_q: 1, pygame.K_d: 0}
            
        if event == pygame.K_d and self.movement_possibilities[pygame.K_d]:
            direction = [tileset, 0]
            self.Move(direction)
            self.movement_possibilities = {pygame.K_z: 1, pygame.K_s: 1, pygame.K_q: 0, pygame.K_d: 1}