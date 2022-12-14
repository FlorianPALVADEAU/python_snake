import pygame

class Sounds:
    def PlaySound(self, sound):
        soundd = pygame.mixer.Sound(f"SnakeGame/sounds/{sound}.mp3")
        pygame.mixer.Sound.play(soundd)
    def PlayMusic(self, sound):
        soundd = pygame.mixer.music.load(f"SnakeGame/sounds/{sound}.mp3")
        pygame.mixer.music.play(soundd)
    def StopMusic():
        pygame.mixer.music.pause()  