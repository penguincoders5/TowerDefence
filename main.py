import pygame
from Map import Map

#Constants
WIDTH = 1200
HEIGHT = 800

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
        # Section: Game & Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            m.clickFind(pygame.mouse.get_pos())

        # Section: Key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                print('WRITE MODE')
                m.writeMode = True
            if event.key == pygame.K_r:
                print('SAVED')
                m.saveMap()



    pygame.time.wait(1)
    pygame.display.update()

#End of Game