# pygame.MOUSEBUTTONDOWN
# pygame.MOUSEBUTTONUP
# pygame.MOUSEMOTION
# pygame.MOUSEWHEEL

import pygame

pygame.init()

pygame.mouse.set_visible(False)  # скрываем курсор

WIDTH, HEIGHT = 600, 400
user_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("События от клавиатуры")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

start_position = None

user_screen.fill(WHITE)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    user_screen.fill(WHITE)

    position = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        pygame.draw.circle(user_screen, BLUE, position, 7)

    pressed = pygame.mouse.get_pressed(3)

    if pressed[0]:
        if start_position is None:
            start_position = position

        width = position[0] - start_position[0]
        height = position[1] - start_position[1]

        user_screen.fill(WHITE)
        pygame.draw.rect(user_screen, RED, (start_position[0], start_position[1], width, height))

    else:
        start_position = None

    pygame.display.update()
    clock.tick(FPS)
