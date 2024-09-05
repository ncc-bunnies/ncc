import pygame,os

# 초기화
pygame.init()
os.system('cls')

# 스크린 설정
screen_width=1280
screen_height=720
screen=pygame.display.set_mode((screen_width,screen_height))

# FPS 설정용
clock=pygame.time.Clock()

# 제목 설정
pygame.display.set_caption('응애')

# 현재 파일의 디렉토리 기준으로 경로 설정
current_dir=os.path.dirname(__file__)
image_dir=os.path.join(current_dir,'image_yhs')

# 배경 설정
background=pygame.image.load(os.path.join(image_dir,'background_side.png'))

# 캐릭터 설정
character=pygame.image.load(os.path.join(image_dir,'character.png'))
char_size=character.get_rect().size
char_width=char_size[0]
char_height=char_size[1]

# 바닥 설정
floor=screen_height-char_height-305

char_x_pos=(screen_width/2)-(char_width/2)
char_y_pos=floor

# 이동 속도
char_speed=0.75

# 이동 변수 초기화
char_x_to=0

# 점프 관련 변수
jump_active=False
jump_speed=0
jump_max=15
gravity=1

# 게임 켜지면 실행할 놈들
running=True
while running:

    # 틱 설정
    dt=clock.tick(60)

    for event in pygame.event.get():

        # X 눌러야 게임 꺼짐
        if event.type==pygame.QUIT:
            running=False

        # 키보드 눌렸을 때
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                char_x_to-=char_speed
            elif event.key==pygame.K_RIGHT:
                char_x_to+=char_speed
            elif event.key==pygame.K_UP and not jump_active:  # 점프 중이 아닐 때만 점프 가능
                jump_active=True
                jump_speed=jump_max

        # 키보드 떼졌을 때
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                char_x_to=0

    # 캐릭터 좌표 변환 (*dt는 속도 보정값)
    char_x_pos+=char_x_to*dt

    # 점프 로직
    if jump_active:
        char_y_pos-=jump_speed  # 점프할 때 위로 올라감
        jump_speed-=gravity  # 속도 감소 (중력 효과)
        
        # 바닥에 닿으면 점프 종료
        if char_y_pos>=floor:
            char_y_pos=floor
            jump_active=False

    # x좌표 제한
    if char_x_pos<0:
        char_x_pos=0
    elif char_x_pos>screen_width-char_width:
        char_x_pos=screen_width-char_width

    # 애들 위치
    screen.blit(background,(0,0))
    screen.blit(character,(char_x_pos,char_y_pos))
    pygame.display.update()

# while문 끝나면(X 누르면) 게임 종료
pygame.quit()