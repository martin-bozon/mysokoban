import pygame
import LARGEUR from config
import HAUTEUR from config
import TITRE from config
#initalise les modules pour pygame
pygame.init()

screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)
background = pygame.image.load("img/sol.jpg")

screen.blit(background, (0,0))

_grille = Grille("matrice.txt")
_grille.drawMap(screen)

pygame.display.flip()