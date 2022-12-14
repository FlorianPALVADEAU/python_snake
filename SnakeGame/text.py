import pygame

class Text:
    def __init__(self, score, position):
        self.font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 32)
        self.score = score
        self.position = position
    def DisplayScore(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, self.position)
    def DisplayLooseMessage(self, screen, score):
        text1 = pygame.font.Font('Oswald-VariableFont_wght.ttf', 32).render(f"Dommage ! Ton score est de {score} !", True, (255, 255, 255))
        text = pygame.font.Font('Oswald-VariableFont_wght.ttf', 32).render(f"Pour rejouer, appuies sur ta touche 'P' !", True, (255, 255, 255))
        text2 = pygame.font.Font('Oswald-VariableFont_wght.ttf', 32).render(f"Si tu souhaites quitter, appuies sur 'Echap' !", True, (255, 255, 255))
        screen.blit(text1, (320, 300))
        screen.blit(text, (250, 400))
        screen.blit(text2, (250, 700))
        