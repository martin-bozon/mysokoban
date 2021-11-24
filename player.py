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

    def drawPlayer(self, screen):
        screen.blit(self.position, (self.x * SIZE, self.y * SIZE))

    def move(self, key):
        if key == K_LEFT:
            self.position = self.gauche
            if not self.check_collision():
                self.x -= 1
        elif key == K_RIGHT:
            self.position = self.droite
            if not self.check_collision():
                self.x += 1
        elif key == K_UP:
            self.position = self.haut
            if not self.check_collision():
                self.y -= 1
        elif key == K_DOWN:
            self.position = self.bas
            if not self.check_collision():
                self.y += 1

    def check_collision(self):
        self.hauty = self.y - 1
        self.basy = self.y + 1
        self.droitex = self.x + 1
        self.gauchex = self.x - 1

        for y in range(len(self.grille.lvtest)):
            for x in range(len(self.grille.lvtest[y])):
                # gauche
                if self.position == self.gauche:
                    pos_grille = self.grille.lvtest[self.y][self.gauchex]
                    if pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF:
                        g = self.grille.move_caisse(self.x, self.y, "gauche")
                        if g:
                            self.x = self.gauchex
                    return pos_grille == MUR or pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF
                # droite
                elif self.position == self.droite:
                    pos_grille = self.grille.lvtest[self.y][self.droitex]
                    if pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF:
                        g = self.grille.move_caisse(self.x, self.y, "droite")
                        if g:
                            self.x = self.droitex
                    return pos_grille == MUR or pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF
                # haut
                elif self.position == self.haut:
                    pos_grille = self.grille.lvtest[self.hauty][self.x]
                    if pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF:
                        g = self.grille.move_caisse(self.x, self.y, "haut")
                        if g:
                            self.y = self.hauty
                    return pos_grille == MUR or pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF
                # bas
                elif self.position == self.bas:
                    pos_grille = self.grille.lvtest[self.basy][self.x]
                    if pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF:
                        g = self.grille.move_caisse(self.x, self.y, "bas")
                        if g:
                            self.y = self.basy
                    return pos_grille == MUR or pos_grille == CAISSE or pos_grille == CAISSE_OBJECTIF


