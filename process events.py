import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
user_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("События от клавиатуры")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

x = WIDTH // 2
y = HEIGHT // 2
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:  # или if event.type == pygame.KEYDOWN:
        x -= speed           #          if event.key == pygame.K_LEFT:
    elif keys[pygame.K_RIGHT]:  #           x -= speed
        x += speed

    user_screen.fill(WHITE)
    pygame.draw.rect(user_screen, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)
