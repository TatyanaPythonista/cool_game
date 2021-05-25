# класс Rect - класс для операции с прямоугольными областями вокруг объекта

import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

user_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Класс Rect')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

ground = HEIGHT-70
jump_force = 20
move = jump_force+1

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=WIDTH//2)
rect.bottom = ground

rect_update = pygame.Rect(rect.x, 0, rect.width, ground)

user_screen.fill(WHITE)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force

    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force+1

    user_screen.fill(WHITE)
    user_screen.blit(hero, rect)
    pygame.display.update(rect_update)

    clock.tick(FPS)
