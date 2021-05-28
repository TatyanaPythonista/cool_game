from random import randint

import pygame
from ball import Ball

pygame.init()

pygame.time.set_timer(pygame.USEREVENT, 2000)

WIDTH = 1000
HEIGHT = 570

user_screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

score = pygame.image.load('image/score_fon.png').convert_alpha()
font = pygame.font.SysFont('arial', 30)

dray = pygame.image.load('image/dray.png').convert_alpha()
dray_rect = dray.get_rect(centerx=WIDTH//2, bottom=HEIGHT-5)

balls_data = [{'path': 'ball_bear.png', 'score': 100},
              {'path': 'ball_fox.png', 'score': 150},
              {'path': 'ball_panda.png', 'score': 200}]

balls_surf = [pygame.image.load('image/'+data['path']).convert_alpha() for data in balls_data]


def create_ball(group):
    index = randint(0, len(balls_surf)-1)
    x = randint(20, WIDTH-20)
    speed = randint(1, 4)
    return Ball(x, speed, balls_surf[index], balls_data[index]['score'], group)


game_score = 0


def collide_balls():
    global game_score
    for ball in balls:
        if dray_rect.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()


balls = pygame.sprite.Group()

background = pygame.image.load('image/back1.jpg').convert()

speed = 10
create_ball(balls)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            create_ball(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dray_rect.x -= speed
        if dray_rect.x < 0:
            dray_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        dray_rect.x += speed
        if dray_rect.x > WIDTH-dray_rect.width:
            dray_rect.x = WIDTH-dray_rect.width

    collide_balls()

    user_screen.blit(background, (0, 0))
    user_screen.blit(score, (0, 0))
    user_screen_text = font.render(str(game_score), True, (94, 138, 14))
    user_screen.blit(user_screen_text, (20, 10))
    balls.draw(user_screen)
    user_screen.blit(dray, dray_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(HEIGHT)


