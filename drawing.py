import pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
user_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Графические примитивы")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.draw.rect(user_screen, BLUE, (10, 10, 50, 100), 2)
# аргументы: поверхность, на которой рисуем, цвет (R, G, B), размер (x - направлен вправо, у - вниз,
# width, height), толщина линии (если ее нет, то закрашиваю всю поверхность)

pygame.draw.line(user_screen, GREEN, (200, 20), (350, 50))
pygame.draw.aaline(user_screen, GREEN, (200, 40), (350, 70))  # сглаженная линия (MAX толщина 1px)

pygame.draw.lines(user_screen, RED, True, [(200, 80), (250, 80), (300, 200)], 2)  # ломанная линия. True - замкнуть
pygame.draw.lines(user_screen, RED, True, [(300, 80), (350, 80), (400, 200)])  # ломанная сглаженная линия.

pygame.draw.polygon(user_screen, WHITE, [[150, 210], [180, 250], [90, 290], [30, 230]])  # нет толщ линии - закрашенный
pygame.draw.polygon(user_screen, WHITE, [[150, 310], [180, 350], [90, 390], [30, 330]], 1)

pygame.draw.circle(user_screen, BLUE, (300, 250), 40)  # координаты центра и радиус
pygame.draw.ellipse(user_screen, BLUE, (300, 300, 100, 50), 1) # прямоугольник, в котором рисуется эллипс, толщина линии

pi = 3.14
pygame.draw.arc(user_screen, RED, (450, 30, 50, 150), pi, 2*pi, 5)  # прямоугольник, в котором рисуется дуга,
# начальный угол, конечный угол, толщина линии

pygame.display.flip()  # получаю отрисованное изображение из буфера
# можно использовать  pygame.display.update(rectangle) - указываю конкретную область перерисовки

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

