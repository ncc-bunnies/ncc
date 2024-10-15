#길상현 코드
import pygame

pygame.init() #초기화

#화면크기
가로 = 480 # 가로 크기
세로 = 640 
크기 = [가로,세로]
pygame.display.set_mode((크기))

프레임 = pygame.time.Clock()

폰트글꼴 = "C:\Users\ncc7\Desktop\khj\ncc\gsh\GabiaBombaram\GabiaBombaram\gabia_bombaram.ttf"
폰트크기 = 20
폰트 = pygame.font.Font(폰트글꼴,폰트크기)

게임 = pygame.display.set_caption("오딘마지막전사")

오딘 = True
while 오딘:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            오딘 = False

    프레임.tick (60)

