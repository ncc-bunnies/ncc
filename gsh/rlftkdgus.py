
import pygame
import time

pygame.init()  # 초기화

# 화면 크기
가로 = 1000  # 가로 크기
세로 = 640 
크기 = [가로, 세로]
화면 = pygame.display.set_mode(크기)

프레임 = pygame.time.Clock()

폰트글꼴 = "C:/Windows/Fonts/malgun.ttf"
폰트크기 = 20
폰트 = pygame.font.Font(폰트글꼴, 폰트크기)

pygame.display.set_caption("오딘 마지막 전사")

오딘 = True
폰트출력 = ""  # 초기화
start_time = "기록"  # 타이머 초기화

while 오딘:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            오딘 = False
        elif event.type == pygame.KEYDOWN:
            if start_time is "기록":  # 타이머가 시작되지 않았다면
                start_time = time.time()  # 현재 시간을 기록
            폰트출력 = f"pygame.KEYDOWN: {pygame.key.name(event.key)}"

    if start_time is not "기록" and time.time() - start_time > 1:  # 1초가 지났다면
        폰트출력 = ""  # 출력 초기화
        start_time = "기록"  # 타이머 초기화

    화면.fill((0, 0, 0))  # 화면을 검은색으로 채우기
    폰트색 = 폰트.render(폰트출력, True, (255, 255, 255))
    폰트위치 = 폰트색.get_rect(center=(가로 // 2, 세로 // 2))
    
    화면.blit(폰트색, 폰트위치)
    
    pygame.display.flip()  # 화면 업데이트
    프레임.tick(60)

pygame.quit()  # Pygame 종료

