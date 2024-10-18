#길상현 코드
import pygame
import time
pygame.init() #초기화


#화면크기
가로 = 1000 # 가로 크기
세로 = 640 
크기 = [가로,세로]
화면 = pygame.display.set_mode((크기))

프레임 = pygame.time.Clock()


#폰트
폰트글꼴 = "C:/Windows/Fonts/malgun.ttf"
폰트크기 = 20
폰트 = pygame.font.Font(폰트글꼴,폰트크기)
가로 = 1000 # 가로 크기
세로 = 640 
크기 = [가로,세로]
화면 = pygame.display.set_mode((크기))

프레임 = pygame.time.Clock()


#폰트
폰트글꼴 = "C:/Windows/Fonts/malgun.ttf"
폰트크기 = 20
폰트 = pygame.font.Font(폰트글꼴,폰트크기)
폰트출력 = "pygame.KEYDOWN"

게임 = pygame.display.set_caption("오딘마지막전사")

오딘 = True
폰트출력 = ""

시간 = "start_time"
시간 = "기록"

while 오딘:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            오딘 = False
        elif event.type == pygame.KEYDOWN:
            if 시간 is "기록": 
                시간 = time.time() 
            폰트출력 = f"pygame.KEYDOWN: {pygame.key.name(event.key)}"

    if 시간 is not "기록" and time.time() - 시간 > 0.5:
        폰트출력 = ""
        시간 = "기록"



        
        
        
    화면.fill((0, 0, 0))
    폰트색 = 폰트.render(폰트출력, True, (255, 255, 255))
    폰트위치 = 폰트색.get_rect(center=(가로 // 2, 세로 // 2))
    

    
    화면.blit(폰트색, 폰트위치)

    프레임.tick (60)




    pygame.display.flip()

pygame.quit()
    



#아아ㅏㅇ아ㅏ아아

