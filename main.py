import pygame
from Map import Map

#Constants
HEIGHT = 800
WIDTH = 1200
BG_COLOR = (210, 190, 100)

#Setup Code
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.flip()
running = True

#Game

m = Map(screen, WIDTH, HEIGHT)
m.drawmap()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.time.wait(1)
    pygame.display.update()

#End of Game