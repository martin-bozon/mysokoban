import pygame
from config import *
from pygame.locals import *


class Player:
    def __init__(self, grille):
        self.gauche = pygame.image.load("img/gauche.png")
        self.droite = pygame.image.load("img/droite.png")
        self.bas = pygame.image.load("img/bas.png")
        self.haut = pygame.image.load("img/haut.png")

        self.position = self.droite
        self.grille = grille
        self.pos = self.grille.getPlayerPosition(self.grille)

        self.x = int(self.pos[0] / SIZE)
        self.y = int(self.pos[1] / SIZE)

        self.hauty = self.y - 1
        self.basy = self.y + 1
        self.droitex = self.x + 1
        self.gauchex = self.x - 1

    def drawPlayer(self, screen):
        screen.blit(self.position, (self.x * SIZE, self.y * SIZE))

    def move(self, key):
        if key == K_LEFT:
            self.position = self.gauche
            self.check_collision()
            #self.x -= 1
        elif key == K_RIGHT:
            self.position = self.droite
            self.x += 1
        elif key == K_UP:
            self.position = self.haut
            self.y -= 1
        elif key == K_DOWN:
            self.position = self.bas
            self.y += 1

    def check_collision(self):
        for y in range(len(self.grille.lvtest)):
            for x in range(len(self.grille.lvtest[y])):
                if self.position == self.gauche:
                    pos_grille = self.grille.lvtest[self.y][self.gauchex]
                    if pos_grille == [self.y, 0]:
                        self.x = -1

