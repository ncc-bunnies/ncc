#길상현 코드
import pygame

pygame.init() #초기화

#화면크기
screen_width = 480 # 가로 크기
screen_height = 640 
pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("")

오딘 = True
while 오딘:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            전원 = False

    프레임.tick (60)