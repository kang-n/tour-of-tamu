import pygame
import quiz1 as q1
import quiz2 as q2
import quiz3 as q3
import quiz4 as q4
import quiz5 as q5
import quiz6 as q6

def mainGame():
    class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

    class User(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.fimages = []
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))

            self.fimages.append(pygame.image.load('sprites/front-right.png'))
            self.fimages.append(pygame.image.load('sprites/front-right.png'))
            self.fimages.append(pygame.image.load('sprites/front-right.png'))
            self.fimages.append(pygame.image.load('sprites/front-right.png'))
            self.fimages.append(pygame.image.load('sprites/front-right.png'))

            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))
            self.fimages.append(pygame.image.load('sprites/front-mid.png'))

            self.fimages.append(pygame.image.load('sprites/front-left.png'))
            self.fimages.append(pygame.image.load('sprites/front-left.png'))
            self.fimages.append(pygame.image.load('sprites/front-left.png'))
            self.fimages.append(pygame.image.load('sprites/front-left.png'))
            self.fimages.append(pygame.image.load('sprites/front-left.png'))

            self.bimages = []
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))

            self.bimages.append(pygame.image.load('sprites/back-right.png'))
            self.bimages.append(pygame.image.load('sprites/back-right.png'))
            self.bimages.append(pygame.image.load('sprites/back-right.png'))
            self.bimages.append(pygame.image.load('sprites/back-right.png'))
            self.bimages.append(pygame.image.load('sprites/back-right.png'))

            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))
            self.bimages.append(pygame.image.load('sprites/back-mid.png'))

            self.bimages.append(pygame.image.load('sprites/back-left.png'))
            self.bimages.append(pygame.image.load('sprites/back-left.png'))
            self.bimages.append(pygame.image.load('sprites/back-left.png'))
            self.bimages.append(pygame.image.load('sprites/back-left.png'))
            self.bimages.append(pygame.image.load('sprites/back-left.png'))

            self.index = 0

            self.image = self.fimages[self.index]
            self.rect = self.fimages[self.index].get_rect(center=(x, y))

        def move(self, x, y):

            self.index += 1
            if self.index >= len(self.fimages) or self.index >= len(self.bimages):
                self.index = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] and user.rect.y > 0:
                user.rect.y -= 3

                self.image = self.bimages[self.index]

            if pressed[pygame.K_DOWN] and user.rect.y < 992 - 32:
                user.rect.y += 3

                self.image = self.fimages[self.index]

            if pressed[pygame.K_LEFT] and user.rect.x > 0:
                user.rect.x -= 3

                self.image = self.fimages[self.index]

            if pressed[pygame.K_RIGHT] and user.rect.x < 880 - 32:
                user.rect.x += 3

                self.image = self.fimages[self.index]

    class Building(pygame.sprite.Sprite):
        def __init__(self, x, y, b1):
            super().__init__()

            self.image = b1
            self.rect = self.image.get_rect(center=(x, y))

    pygame.init()
    screen = pygame.display.set_mode((992, 880))
    done = False

    corp = pygame.image.load("labels\corpsquad.png").convert()
    kyle = pygame.image.load("labels\Kyle Field.png").convert()
    mem = pygame.image.load("labels\Memorial Student Center .png").convert()
    mil = pygame.image.load("labels\Military Walk Seal .png").convert()
    wil = pygame.image.load("labels\wil.png").convert()
    bon = pygame.image.load("labels\onf.png").convert()

    x = 100
    y = 100

    clock = pygame.time.Clock()

    all_sprites_list = pygame.sprite.Group()

    user = User(x, y)
    corps = Building(390, 570, corp)
    kylef = Building(180, 530, kyle)
    memo = Building(150, 460, mem)
    mili = Building(210, 350, mil)
    will = Building(270, 820, wil)
    bonf = Building(770, 240, bon)

    all_sprites_list.add(user)
    all_sprites_list.add(corps)
    all_sprites_list.add(kylef)
    all_sprites_list.add(mili)
    all_sprites_list.add(memo)
    all_sprites_list.add(will)
    all_sprites_list.add(bonf)

    clock = pygame.time.Clock()

    bg = pygame.image.load("tamu map.png")
    BackGround = Background('tamu map.png', [0, 0])

    ua1 = True
    ua2 = True
    ua3 = True
    ua4 = True
    ua5 = True
    ua6 = True

    sc = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        all_sprites_list.update()
        all_sprites_list.draw(screen)

        user.move(x, y)

        if (pygame.sprite.collide_rect(user, corps) and ua1):
            if q2.quiz2():
                sc += 1
                print(sc)

            screen.fill([255, 255, 255])
            screen.blit(BackGround.image, BackGround.rect)

            user.rect.x -= 10
            user.rect.y -= 10

            all_sprites_list.update()
            all_sprites_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()

            ua1 = False

        if (pygame.sprite.collide_rect(user, kylef) and ua2):
            if q6.quiz6():
                sc += 1
                print(sc)

            screen.fill([255, 255, 255])
            screen.blit(BackGround.image, BackGround.rect)

            user.rect.x -= 10
            user.rect.y -= 10

            all_sprites_list.update()
            all_sprites_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()

            ua2 = False

        if (pygame.sprite.collide_rect(user, will) and ua3):
            if q5.quiz5():
                sc += 1
                print(sc)

            screen.fill([255, 255, 255])
            screen.blit(BackGround.image, BackGround.rect)

            user.rect.x -= 10
            user.rect.y -= 10

            all_sprites_list.update()
            all_sprites_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()

            ua3 = False

        if (pygame.sprite.collide_rect(user, mili) and ua4):
            if q3.quiz3():
                sc += 1
                print(sc)

            screen.fill([255, 255, 255])
            screen.blit(BackGround.image, BackGround.rect)

            user.rect.x -= 10
            user.rect.y -= 10

            all_sprites_list.update()
            all_sprites_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()

            ua4 = False

        if (pygame.sprite.collide_rect(user, memo) and ua5):
            if q4.quiz4():
                sc += 1
                print(sc)

            screen.fill([255, 255, 255])
            screen.blit(BackGround.image, BackGround.rect)

            user.rect.x -= 10
            user.rect.y -= 10

            all_sprites_list.update()
            all_sprites_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()

            ua5 = False

        if (pygame.sprite.collide_rect(user, bonf) and ua6):
            if q1.quiz1():
                sc += 1
                print(sc)

            screen.fill([255, 255, 255])
            screen.blit(BackGround.image, BackGround.rect)

            user.rect.x -= 10
            user.rect.y -= 10

            all_sprites_list.update()
            all_sprites_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()

            ua6 = False

        if (not ua1) and (not ua2) and (not ua3) and (not ua4) and (not ua5) and (not ua6):
            done = True

        pygame.display.flip()
        pygame.display.update()
        clock.tick(40)

    return sc
