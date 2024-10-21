import pygame
import random

# 게임 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("타워 디펜스 게임")

# 색상 정의
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 타워 클래스
class Tower:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# 적 클래스
class Enemy:
    def __init__(self, path):
        self.path = path
        self.index = 0
        self.rect = pygame.Rect(path[0][0], path[0][1], 50, 50)  # 수정된 부분
        self.speed = 2

    def move(self):
        if self.index < len(self.path) - 1:
            target = self.path[self.index + 1]
            if self.rect.x < target[0]:
                self.rect.x += self.speed
            elif self.rect.x > target[0]:
                self.rect.x -= self.speed
            if self.rect.y < target[1]:
                self.rect.y += self.speed
            elif self.rect.y > target[1]:
                self.rect.y -= self.speed
            
            # 다음 경로 점으로 이동
            if self.rect.topleft == target:
                self.index += 1

        # 적이 마지막 경로 점에 도달하면 True를 반환
        return self.index == len(self.path) - 1 and self.rect.topleft == self.path[-1]

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# 경로 정의
path = [(0, 300), (200, 300), (200, 100), (600, 100), (600, 300), (800, 300)]

# 게임 루프
def main():
    clock = pygame.time.Clock()
    running = True
    towers = []
    enemies = []

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 마우스 클릭 시 타워 생성
                if event.button == 1:  # 왼쪽 버튼 클릭
                    towers.append(Tower(event.pos[0], event.pos[1]))

        # 적 생성
        if random.randint(1, 100) == 1:  # 생성 빈도 조절
            enemies.append(Enemy(path))

        # 적 이동 및 그리기
        for enemy in enemies[:]:
            if enemy.move():
                enemies.remove(enemy)  # 마지막 경로 점에 도달한 적 제거
            enemy.draw()

        # 타워 그리기
        for tower in towers:
            tower.draw()

        pygame.display.flip()

        # FPS 설정
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("에러가 발생했습니다:", e)
