import pygame
import random

class Map:
    def __init__(self, screen, w, h):
        self.w = w
        self.h = h
        self.screen = screen
        self.gridsize = 100

        self.map = []
        for i in range(self.h//self.gridsize):
            row = []
            for j in range(self.w//self.gridsize):
                row.append(0)
            self.map.append(row)


        # map_encoding = [0, 10, 12]
        # self.generatemap(map_encoding)

    def drawmap(self):

        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                pygame.draw.rect(self.screen, (random.randint(0, 255), 100, 100), pygame.Rect(j*self.gridsize, i*self.gridsize, self.gridsize, self.gridsize))

                if self.map[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(j*self.gridsize, i*self.gridsize, self.gridsize, self.gridsize))

    def generatemap(self, encoding):
        r = 0
        for n in encoding:

            if n < len(self.map[0]):
                self.map[0][n] = 1
            else:
                while n >= len(self.map[0]):
                    n -= len(self.map[0])
                    r += 1

                    self.map[r][n] = 1

    def draw(self, x, y):
        print('x:', x, ' y:',y)
        xi = x/self.gridsize
        yi = y/self.gridsize
        print('xi:', xi, ' yi:',yi)
