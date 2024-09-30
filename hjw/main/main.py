# 라이브러리 import
import pygame

# 파이게임 설정
pygame.init()

# 게임 화면
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 게임 화면 노래

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Castle Defender")

clock = pygame.time.Clock()
FPS = 60


bg = pygame.image.load('img/bg.png').convert_alpha()

# 게임 반복
run = True
while True:

    clock.tick(FPS)

    screen.blit(bg, (0, 0))


    # 이벤트 핸들러
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 화면 새로고침
    pygame.display.update()

pygame.quit()
