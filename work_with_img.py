import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

user_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Изображения')

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

car_surf = pygame.image.load('image/car.bmp').convert()
# convert  - метод поверхности, возвращает изображение с пикселями в базовым формате.
# blit сработает быстрее.
car_rect = car_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
car_surf.set_colorkey((255, 255, 255))
# если нужно сделать прозрачный фон то у объекта surf вызываем метод .set_colorkey((код цвета в Rbn)) -
# - этот цвет станет прозрачным, но для png это не актуально, т.к. png поддерживать прозрачность
bg_surf = pygame.image.load("image/pesok-img.jpg").convert_alpha() # как convert, но с учетом alpha-каналов
user_screen.blit(bg_surf, (0, 0))
user_screen.blit(car_surf, car_rect)
pygame.display.update()

# pygame.transform - трансформируем поверхности

# pygame.transform.scale(Surfase, (width, height), DestSurfase=None) -> None

car_up = car_surf
car_down = pygame.transform.flip(car_surf, False, True)
car_left = pygame.transform.rotate(car_surf, 90)
car_right = pygame.transform.rotate(car_surf, -90)

car = car_up
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    button = pygame.key.get_pressed()
    if button[pygame.K_LEFT]:
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    elif button[pygame.K_RIGHT]:
        car = car_right
        car_rect.x += speed
        if car_rect.x > WIDTH - car_rect.height:
            car_rect.x = WIDTH - car_rect.height
    elif button[pygame.K_UP]:
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif button[pygame.K_DOWN]:
        car = car_down
        car_rect.y += speed
        if car_rect.y > HEIGHT - car_rect.height:
            car_rect.y = HEIGHT - car_rect.height

    user_screen.blit(bg_surf, (0, 0))
    user_screen.blit(car, car_rect)

    pygame.display.update()

    clock.tick(FPS)
