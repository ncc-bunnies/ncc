import pygame
import os

# 초기화
pygame.init()
os.system('cls')

# 스크린 설정
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

# FPS 설정용
clock=pygame.time.Clock()

# 제목 설정
pygame.display.set_caption('응애')

# 현재 파일의 디렉토리 기준으로 경로 설정(by ChatGPT)
current_dir=os.path.dirname(__file__)
image_dir=os.path.join(current_dir,"image_yhs")

# 배경 설정
background=pygame.image.load(os.path.join(image_dir,'background.png'))

# 캐릭터 설정
character=pygame.image.load(os.path.join(image_dir,'character.png'))
char_size=character.get_rect().size
char_width=char_size[0]
char_height=char_size[1]
char_x_pos=(screen_width/2)-(char_width/2)
char_y_pos=screen_height-char_height-100

# 적 설정
enemy=pygame.image.load(os.path.join(image_dir,'enemy.png'))
enemy_size=enemy.get_rect().size
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=(screen_width/2)-(enemy_width/2)
enemy_y_pos=screen_height-enemy_height-200

# 이동 속도
char_speed=0.75

# 이동 변수 초기화
to_x=0
to_y=0

# 게임 켜지면 실행할 놈들
running=True
while running:

    # 틱 설정
    dt=clock.tick(120)
    print('FPS:',str(format(clock.get_fps(),'.1f')))

    for event in pygame.event.get():

        # X 눌러야 게임 꺼짐
        if event.type==pygame.QUIT:
            running=False

        # 키보드 눌렸을 때
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                to_y-=char_speed
            elif event.key==pygame.K_DOWN:
                to_y+=char_speed
            elif event.key==pygame.K_LEFT:
                to_x-=char_speed
            elif event.key==pygame.K_RIGHT:
                to_x+=char_speed

        # 키보드 떼졌을 때
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0
            elif event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0

    # 캐릭터 좌표 변환 (*dt는 속도 보정값)
    char_x_pos+=to_x*dt
    char_y_pos+=to_y*dt

    # x좌표 제한
    if char_x_pos<0:
        char_x_pos=0
    elif char_x_pos>screen_width-char_width:
        char_x_pos=screen_width-char_width

    # y좌표 제한
    if char_y_pos<320:
        char_y_pos=320
    elif char_y_pos>screen_height-char_height:
        char_y_pos=screen_height-char_height

    # 충돌 처리
    char_rect=character.get_rect()
    char_rect.left=char_x_pos
    char_rect.top=char_y_pos

    # 배경이랑 캐릭터 위치
    screen.blit(background,(0,0))
    screen.blit(character,(char_x_pos,char_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    pygame.display.update()

# while문 끝나면(X 누르면) 게임 종료
pygame.quit()
