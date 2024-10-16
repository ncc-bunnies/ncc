#길상현 코드
import pygame

pygame.init()


screen_width = 480
screen_height = 640 
pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("아")

전원 = True

while 전원:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            전원 = False

