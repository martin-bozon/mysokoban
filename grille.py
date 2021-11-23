# -*- coding: utf-8 -*-
import pygame
from config import *

class Grille:
    def __init__(self, fichier):
        self.ref_img = {
            MUR: pygame.image.load("img/mur.png"),
            CAISSE: pygame.image.load("img/banane.png"),
            OBJECTIF: pygame.image.load("img/objectif.png"),
            #CAISSE_OK: pygame.image.load("img/caisse_ok.jpg"),
        }
        with open(fichier, 'r') as fich:
            self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]

        self.coord_objec = []
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == OBJECTIF:
                    self.coord_objec.append((x, y))

    def drawMap(self, screen):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                img = self.lvtest[y][x]
                if img in (VIDE, PLAYER):
                    x += 1
                else:
                    screen.blit(self.ref_img[img], (x * SIZE, y * SIZE))

    def is_fini(self):
        lis = [self.lvtest[y][x] for (x, y) in self.coord_objec]
        return lis.count(CAISSE_OBJECTIF) == len(self.coord_objec)

    def getPlayerPosition(self, grille):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == PLAYER:
                    return (x * SIZE, y * SIZE)


if __name__ == '__main__':
    g = Grille()
    g.genMap("matrice.txt")
