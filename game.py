import pygame
import time
import random
import mainmap as m

pygame.init()

display_width = 992
display_height = 880

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
maroon = (128,0,0)
gray = (144, 145, 148)

uX = 100
uY = 100
score = 0

tamu_png = pygame.image.load('tamu slide.png')
reveille = pygame.image.load('Reveille Victory Screen 300x300.png')


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('TAMU_Logo.png')



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                python.quit()
                quit()
            else:
                t.mainGame(uX,uY)
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(maroon)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Tour TAMU", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(tamu_png, (0, 0))
        button("START", 250 ,700, 100, 50, white, gray, "play")
        button("QUIT", 650, 700, 100, 50, white, gray, "quit")

        pygame.display.update()
        clock.tick(15)

def game_end(score):
    end = True

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        score_statement = "Your Score Is: " + str(score)
        gameDisplay.fill(maroon)
        text = pygame.font.Font('freesansbold.ttf', 35)
        TextSurf, TextRect = text_objects("Congrats! You Have Finished Your Tour!", text)
        TextSurf, TextRect = text_objects(score_statement, text)
        gameDisplay.blit(reveille, (350,250))
        TextRect.center = ((display_width / 2), (200))
        gameDisplay.blit(TextSurf, TextRect)

        button("EXIT", 435, 700, 100, 50, white, gray, "quit")

        pygame.display.update()
        clock.tick(15)


def game_loop():
    score = m.mainGame()
    game_end(score)


game_intro()
game_loop()
pygame.quit()
quit()