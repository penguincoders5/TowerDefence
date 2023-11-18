import pygame

class GUI:
    def __init__(self, screen, pos, c, hc):
        self.screen = screen
        self.x, self.y = pos
        self.c = c
        self.hc = hc
        pygame.draw.rect(screen, self.c, pygame.Rect(self.x, self.y, 200, 50))
