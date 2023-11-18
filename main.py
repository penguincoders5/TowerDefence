import pygame
from Map import Map
from GUI import GUI



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




#ADDED FEATURES

TEXT_COLOR = (0, 255, 255)
TEXT_BG_COLOR = (255, 0, 255)

pygame.display.set_caption('Tower Defence Development and Experiment')
font = pygame.font.Font('freesansbold.ttf', 20)

text = font.render('GeeksForGeeks', True, TEXT_COLOR, TEXT_BG_COLOR)
font.render

textSetter = lambda s: font.render(s, True, TEXT_COLOR, TEXT_BG_COLOR)

def addText(s, pos):
    text = textSetter(s)
    textRect = text.get_rect()
    textRect.center = pos
    screen.blit(text, textRect)


m = Map(screen, WIDTH, HEIGHT)
m.drawmap()

button1 = GUI(screen, (100, 100), (170,170,170), (100,100,100))


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
                addText('Write Mode', (100, HEIGHT - 50))
                addText('R to save map', (100, HEIGHT - 25))
                print('WRITE MODE')
                m.writeMode = True
            if event.key == pygame.K_r:
                title = input('Name: ')
                print('nextline')
                m.saveMap(title)
                running = False
            if event.key == pygame.K_o:
                m.loadMap()



    pygame.time.wait(1)
    pygame.display.update()

#End of Game