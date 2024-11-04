import pygame

pygame.init() #초기화

#화면크기
screen_width = 480 # 가로 크기
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("bunnies")

h = pygame.image.load("C:\\Users\\ncc7\\Desktop\\khj\\ncc\\hwijun\\asset\\gg.png")

cha = pygame.image.load("C:\\Users\\ncc7\\Desktop\\khj\\ncc\\hwijun\\asset\\cha.png")
cha_size = cha.get_rect().size
cha_width = cha_size[0]
cha_height = cha_size[1]
cha_x_pos = screen_width / 2
cha_y_pos = screen_height - cha_height


running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False

    screen.blit(h, (0, 0))
    screen.blit(cha,(cha_x_pos,cha_y_pos) )
    pygame.display.update()




pygame.quit()