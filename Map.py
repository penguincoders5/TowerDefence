import pygame
import random

class Map:
    def __init__(self, screen, w, h):
        self.w = w
        self.h = h
        self.screen = screen
        self.gridsize = 100

        self.map = []
        for i in range(self.w//self.gridsize):
            row = []
            for j in range(self.h//self.gridsize):
                row.append(0)
            self.map.append(row)


    def drawmap(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                pygame.draw.rect(self.screen, (random.randint(0, 255), 100, 100), pygame.Rect(i*self.gridsize, j*self.gridsize, self.gridsize, self.gridsize))

