import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

user_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Класс surface")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

surf = pygame.Surface((WIDTH, 200))
bita = pygame.Surface((50, 10))

surf.fill(BLUE)
surf.fill(RED)

bita_x, bita_y = 0, 150
x, y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.fill(BLUE)
    surf.blit(bita, (bita_x, bita_y))

    if bita_x < WIDTH:
        bita_x += 5
    else:
        bita_x = 0

    if y < HEIGHT:
        y += 1
    else:
        y = 0

    user_screen.fill(WHITE)
    user_screen.blit(surf, (x, y))
    pygame.display.update()

    clock.tick(FPS)

