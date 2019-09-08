import pygame
import time
import random
def quiz2():
    pygame.init()

    display_width = 992
    display_height = 880

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    maroon = (128, 0, 0)
    gray = (144, 145, 148)

    gameDisplay = pygame.display.set_mode((display_width, display_height))

    clock = pygame.time.Clock()


    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def button(msg, x, y, w, h, ic, ac, action=None):
        global end
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                if action == "correct":
                    end = False
                    return True
                end = False


        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("freesansbold", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

    global end
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(maroon)
        text = pygame.font.Font('freesansbold.ttf', 35)
        TextSurf, TextRect = text_objects("What song is played by the buglers at Silver Taps?", text)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        a1 = False
        button("Taps", 250, 700, 200, 50, white, gray, "play")
        a1 =button("Silver Taps", 650, 700, 200, 50, white, gray, "correct")

        if a1:
            return True
        pygame.display.update()
        clock.tick(15)