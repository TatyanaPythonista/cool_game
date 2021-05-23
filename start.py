import pygame

pygame.init()

pygame.display.set_mode((600, 400))

flag_running = True

while flag_running:
    for event in pygame.event.get():
        print(pygame.event.get())
        if event.type == pygame.QUIT:
            pygame.quit()
            flag_running = False

print('Game over')
