# -*- coding: utf-8 -*-
import pygame
import MUR from config
import CAISSE from config
import OBJECTIF from config

class Grille:
    def __init__(self):
        self.ref_img = {
            MUR: pygame.image.load("img/mur.png"),
            CAISSE: pygame.image.load("img/banane.png"),
            OBJECTIF: pygame.image.load("img/objectif.png"),
            #CAISSE_OK: pygame.image.load("img/caisse_ok.jpg"),
        }
        with open ('matrice.txt', 'r') as fich:
            self.lvl = [[int(l) for l in line.strip().split(" ")] for line in fich]

        self.coord_objec = []
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == OBJECTIF:
                    self.coord_objec.append((x, y))

    def drawMap:
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                img = self.lvtest[y][x]
                if img in (VIDE, PLAYER):
                    x += 1
                else:
                    screen.blit(self.ref_img[img], (x * SIZE, y * SIZE))
