import pygame

pygame.init()

pygame.display.set_mode((600, 480))
pygame.display.set_caption("정우")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()