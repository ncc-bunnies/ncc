#길상현 코드
import pygame

pygame.init() #초기화

#화면크기
가로 = 1000 # 가로 크기
세로 = 640 
크기 = [가로,세로]
화면 = pygame.display.set_mode((크기))

프레임 = pygame.time.Clock()

폰트글꼴 = "C:/Windows/Fonts/malgun.ttf"
폰트크기 = 20
폰트 = pygame.font.Font(폰트글꼴,폰트크기)
for event in pygame.event.get():
    폰트출력 = "pygame.KEYDOWN"
폰트색 = 폰트.render(폰트출력, True, (255, 255, 255))
폰트위치 = 폰트색.get_rect(center=(가로 // 2, 세로 // 2))

게임 = pygame.display.set_caption("오딘마지막전사")

오딘 = True
while 오딘:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            오딘 = False
    프레임.tick (60)

    화면.blit(폰트색, 폰트위치)





    pygame.display.flip()
    



#아아ㅏㅇ아ㅏ아아