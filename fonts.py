import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

user_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Шрифты')

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

font = pygame.font.Font('fonts/YandexSDLight.ttf', 24)
user_screen_text = font.render("Hello World!", True, RED)
position = user_screen_text.get_rect(center=(WIDTH//2, HEIGHT//2))

user_screen.fill(WHITE)
user_screen.blit(user_screen_text, position)
pygame.display.update()


def draw_text():
    user_screen.fill(WHITE)
    user_screen.blit(user_screen_text, position)
    pygame.display.update()


draw_text()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()

    if pygame.mouse.get_focused() and position.collidepoint(pygame.mouse.get_pos()):
        buttons = pygame.mouse.get_pressed(3)
        if buttons[0]:
            rel = pygame.mouse.get_rel()
            position.move_ip(rel)
            draw_text()

    clock.tick(FPS)
