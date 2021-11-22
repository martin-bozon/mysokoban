import pygame
#initalise les modules pour pygame
pygame.init()
#créer un écran de jeu
screen = pygame.display.set_mode((500, 500))
#Change le title
pygame.display.set_caption('MySokoban')
#import image
image = pygame.image.load(r'./image.jpg')
#affiche l'image
screen.blit(image, (0, 0))

done = False
x = 60
y = 60
is_red = True
clock = pygame.time.Clock()
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #fait se déplacer le carré
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_DOWN]:
        y += 1
    if pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1
    #fait en sorte de pas sortir de l'écran
    if x <= 0:
        x = 0
    elif x >= 400:
        x = 400
    if y >= 400:
        y = 400
    elif y <= 0:
        y = 0
    #reset l'image pour avoir un carré et pas un dessin
    screen.blit(image, (0, 0))
    #Affiche carré sur le jeu
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 90, 90))
    #Rend le jeu visible
    pygame.display.flip()
