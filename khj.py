import pygame

pygame.init() #초기화

#화면크기
screen_width = 480 # 가로 크기
screen_height = 640 
pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("bunnies")

사진 = pygame.image.load("C:\\Users\\ncc7\\Desktop\\khj\\ncc\\hwijun\\asset\\gg.png")


running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
pygame.quit()