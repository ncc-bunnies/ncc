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
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 128, 255)

# 타워 클래스
class Tower:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.attack_range = 200  # 공격 범위
        self.attack_power = 10    # 공격력
        self.attack_cooldown = 60  # 쿨타임 (프레임 수)
        self.cooldown_counter = 0  # 쿨타임 카운터
        self.projectiles = []      # 발사된 구체 리스트

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)
        # 공격 범위 표시
        pygame.draw.circle(screen, YELLOW, self.rect.center, self.attack_range, 1)

    def attack(self, enemies):
        if self.cooldown_counter <= 0:  # 쿨타임이 끝났다면
            for enemy in enemies:
                if self.get_distance(enemy) <= self.attack_range:
                    projectile = Projectile(self.rect.center, enemy)
                    self.projectiles.append(projectile)
                    self.cooldown_counter = self.attack_cooldown  # 쿨타임 설정
                    return 0  # 발사했지만 적을 처치하지 못했으므로 보상은 0
        return 0  # 쿨타임이 끝나지 않은 경우에도 보상은 0

    def get_distance(self, enemy):
        return ((self.rect.centerx - enemy.rect.centerx) ** 2 + (self.rect.centery - enemy.rect.centery) ** 2) ** 0.5

    def update(self, enemies):
        self.cooldown_counter -= 1  # 쿨타임 감소
        self.update_projectiles(enemies)

    def update_projectiles(self, enemies):
        reward = 0  # 보상 초기화
        for projectile in self.projectiles[:]:
            if projectile.move():
                # 적을 맞춘 경우
                enemy = projectile.target
                enemy.health -= self.attack_power  # 적의 체력 감소
                if enemy.health <= 0 and enemy in enemies:
                    enemies.remove(enemy)  # 체력이 0 이하인 적 제거
                    # 보상 설정
                    reward += 20 if not enemy.is_strong else 50  # 일반 적은 20원, 파란 적은 50원
                self.projectiles.remove(projectile)  # 구체 제거
        return reward  # 보상 반환

# 적 클래스
class Enemy:
    def __init__(self, path, is_strong=False):
        self.path = path
        self.index = 0
        self.rect = pygame.Rect(path[0][0], path[0][1], 50, 50)
        self.speed = 2
        self.health = 20 if not is_strong else 300  # 일반 적은 20, 강한 적은 300
        self.is_strong = is_strong  # 강한 적인지 여부

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

        return self.index == len(self.path) - 1 and self.rect.topleft == self.path[-1]

    def draw(self):
        color = LIGHT_BLUE if self.is_strong else RED
        pygame.draw.rect(screen, color, self.rect)

# 구체 클래스
class Projectile:
    def __init__(self, position, target):
        self.rect = pygame.Rect(position[0], position[1], 10, 10)
        self.target = target
        self.speed = 5

    def move(self):
        # 구체를 적 방향으로 이동
        if self.rect.x < self.target.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > self.target.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < self.target.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > self.target.rect.y:
            self.rect.y -= self.speed

        # 구체가 적과 충돌하면 True 반환
        return self.rect.colliderect(self.target.rect)

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# 경로 정의
path = [(0, 300), (200, 300), (200, 100), (600, 100), (600, 300), (800, 300)]

# 게임 루프
def main():
    clock = pygame.time.Clock()
    running = True
    towers = []
    enemies = []
    money = 120  # 초기 자금
    enemy_spawn_time = 60  # 적 소환 간격 (프레임 수, 1초마다 1개 생성)
    enemy_spawn_counter = 0  # 소환 카운터
    insufficient_funds = False  # 돈 부족 플래그
    time_counter = 0  # 시간 카운터
    insufficient_funds_time = 0  # 돈 부족 메시지 표시 시간

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 마우스 클릭 시 타워 설치
                if event.button == 1:  # 왼쪽 버튼 클릭
                    if money >= 100:  # 돈이 충분할 경우
                        towers.append(Tower(event.pos[0], event.pos[1]))
                        money -= 100  # 타워 설치 비용 차감
                        insufficient_funds = False  # 돈 부족 플래그 초기화
                    else:
                        insufficient_funds = True  # 돈 부족 플래그 설정
                        insufficient_funds_time = 120  # 2초 동안 표시하도록 설정

        # 적 생성
        enemy_spawn_counter += 1
        time_counter += 1  # 시간 증가
        if enemy_spawn_counter >= enemy_spawn_time:
            # 일반 적 추가
            enemies.append(Enemy(path))
            enemy_spawn_counter = 0  # 카운터 초기화

        # 20초 후에 파란 적 추가
        if time_counter > 1200:  # 20초 = 20 * 60
            if enemy_spawn_counter >= enemy_spawn_time:
                enemies.append(Enemy(path, is_strong=True))  # 파란 적 추가
                enemy_spawn_counter = 0  # 카운터 초기화

        # 적 이동 및 그리기
        for enemy in enemies[:]:
            if enemy.move():
                enemies.remove(enemy)  # 마지막 경로 점에 도달한 적 제거
            enemy.draw()

        # 타워 공격 및 구체 발사
        for tower in towers:
            reward = tower.attack(enemies)  # 적 감지 및 구체 발사
            reward += tower.update_projectiles(enemies)  # 구체가 적을 맞추었을 때 보상 추가
            if reward > 0:
                money += reward  # 적을 처치했을 때 돈 추가
            tower.update(enemies)   # 타워 업데이트
            tower.draw()

        # 구체 그리기
        for tower in towers:
            for projectile in tower.projectiles:
                projectile.draw()

        # 현재 자금 표시
        font = pygame.font.Font(None, 36)
        money_text = font.render(f'Money: {money}', True, (0, 0, 0))
        screen.blit(money_text, (10, 10))

        # 돈 부족 메시지 표시
        if insufficient_funds_time > 0:
            insufficient_funds_text = font.render("돈이 부족합니다", True, RED)
            screen.blit(insufficient_funds_text, (10, 50))
            insufficient_funds_time -= 1  # 타이머 감소

        pygame.display.flip()

        # FPS 설정
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("에러가 발생했습니다:", e)
