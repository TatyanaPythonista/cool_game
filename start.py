import pygame

pygame.init()

pygame.display.set_mode((600, 400), pygame.RESIZABLE) # вторая константа позволяет менять параметры окна
pygame.display.set_caption('The Cool Game')  # меняю заголовок у игрового окна
pygame.display.set_icon(pygame.image.load('image/app.bmp'))  # меняю иконку у игрового окна

clock = pygame.time.Clock()
# FPS - Frames per second
FPS = 60
flag_running = True

while flag_running:
    for event in pygame.event.get():
        print(pygame.event.get())
        if event.type == pygame.QUIT:
            pygame.quit()
            flag_running = False
    clock.tick(FPS)  # количество итераций в секунду (учитывает срок выполнения цикла)

print('Game over')
