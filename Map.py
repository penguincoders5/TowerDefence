import pygame
import random

RANDOM_MODE = True
DEBUG_MODE = False


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

        self.writeMode = False
        self.encoding = [self.gridsize, [], []]

    def drawmap(self):

        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                c = (random.randint(0, 255), 100, 100) if RANDOM_MODE else (255, 150, 210)
                pygame.draw.rect(self.screen, c, pygame.Rect(j*self.gridsize, i*self.gridsize, self.gridsize, self.gridsize))

                if self.map[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(j*self.gridsize, i*self.gridsize, self.gridsize, self.gridsize))

    def drawTile(self, i, j):
        pygame.draw.rect(self.screen, (0, 0, 0),pygame.Rect(j * self.gridsize, i * self.gridsize, self.gridsize, self.gridsize))
        if self.writeMode:
            self.encoding[1].append(i)
            self.encoding[2].append(j)


    def clickFind(self, pos):
        x,y = pos
        print('x:', x, ' y:',y) if DEBUG_MODE else 0
        col_index = x//self.gridsize
        row_index = y//self.gridsize
        print('col:', col_index, ' row:',row_index) if DEBUG_MODE else 0
        self.drawTile(row_index, col_index)


    def saveMap(self):
        f = open('maps.txt', 'w')
        s = str(self.encoding[0])
        for i in range(1, 3):
            s += '*'
            for c in self.encoding[i]:
                s += str(c) + ' '
        f.write(s)

    def loadMap(self):
        f = open('maps.txt', 'r')
        data = f.read()
        datalist = data.split('*')

        ##COPY AND PASTE FROM INIT to get gridsize
        self.gridsize = int(datalist[0])

        self.map = []
        for i in range(self.h // self.gridsize):
            row = []
            for j in range(self.w // self.gridsize):
                row.append(0)
            self.map.append(row)

        ##setting correct tiles
        xs = datalist[1].split(' ')
        ys = datalist[2].split(' ')


        for i in range(len(xs) - 1):

            print(xs[i], ys[i])
            self.map[int(xs[i])][int(ys[i])] = 1
        self.drawmap()







