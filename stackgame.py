import pygame
import sys

# 파이게임 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stack Game")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 블록 설정
block_width = 100
block_height = 10

# 블록 이동 속도
block_speed = 3

# 점수
score = 0
highest_score = 0
clock = pygame.time.Clock()

class Brick:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = block_width
        self.h = block_height
        self.color = RED
        self.speed = speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed
        if self.x > width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1

def scoreboard():
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(score), True, WHITE)
    screen.blit(text, (200, 10))

def highestboard():
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(highest_score), True, WHITE)
    screen.blit(text, (10, 10))

def close():
    pygame.quit()
    sys.exit()

def game():
    global block_width, block_height, block_speed, score
    loop = True

    block_width = 100
    block_height = 10
    speed = 3
    score = 0
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                
                if event.key == pygame.K_q:
                    close()
        scoreboard()
        highestboard()
        display.fill(BLACK)
        clock.tick(60)

game()
