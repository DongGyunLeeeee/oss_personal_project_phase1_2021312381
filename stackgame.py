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
GREEN = (0, 255, 0)

# 블록 설정
block_width = 100
block_height = 10

# 블록 이동 속도
speed = 3

# 점수
score = 0
highest_score = 0
clock = pygame.time.Clock()

paused = False

# 블록 클래스
class Block:

    # 블록 초기화
    def __init__(self, x, y, color, speed):
        # 블록의 x 좌표
        self.x = x

        # 블록의 y 좌표
        self.y = y

        # 블록의 너비
        self.w = block_width

        # 블록의 높이
        self.h = block_height

        # 블록의 색
        self.color = RED

        # 블록의 속도
        self.speed = speed

    # 블록 그리기
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

    # 블록이 양쪽 화면에 닿으면 방향 전환
    def move(self):
        self.x += self.speed
        if self.x > screen_width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1

# 스택 클래스
class Stack:
    
    # 스택 초기화
    def __init__(self):
        self.stack = []

        # 쌓인 블록 수
        self.initSize = 20

        # 초기 블록 세팅
        for i in range(self.initSize):
            newBlock = Block(150, 590 - i * 10, RED, 0)
            self.stack.append(newBlock)

    # 초기 블록 세팅
    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    # 초기 블록 세팅
    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    # 블록 추가하기
    def adding(self):
        newBlock = Block(0, 390, RED, speed)
        self.initSize += 1
        self.stack.append(newBlock)

    # 블록 쌓기 게임 진행
    def stacking(self):
        # 게임 진행 간 유지되어야 하는 블록 너비, 점수 전역 변수 선언
        global block_width, score, speed

        # 맨위 블록 인덱스
        lowerIndex = self.initSize - 2

        # 쌓일 블록 인덱스
        upperIndex = self.initSize - 1

        # 맨위 블록 선언
        lowerBlock = self.stack[lowerIndex]

        # 쌓일 블록 선언
        upperBlock = self.stack[upperIndex]

        # 블록을 미리 쌓은 경우
        if upperBlock.x <= lowerBlock.x and not (upperBlock.x + upperBlock.w < lowerBlock.x):
            self.stack[upperIndex].w = self.stack[upperIndex].x + self.stack[upperIndex].w - lowerBlock.x
            self.stack[upperIndex].x = lowerBlock.x
            if self.stack[upperIndex].w > lowerBlock.w:
                self.stack[upperIndex].w = lowerBlock.w
            self.stack[upperIndex].speed = 0
            score += 1

        # 블록을 늦게 쌓은 경우
        elif lowerBlock.x <= upperBlock.x <= lowerBlock.x + lowerBlock.w:
            self.stack[upperIndex].w = lowerBlock.x + lowerBlock.w - upperBlock.x
            self.stack[upperIndex].speed = 0
            score += 1
        
        # 겹치는 지점이 없게 쌓은 경우
        else:
            ending()
        
        # 한 블록 쌓일 때마다 스택 한 블록씩 내리기
        for i in range(self.initSize):
            self.stack[i].y += 10

        # 블록 너비 갱신
        block_width = self.stack[upperIndex].w

# 현재 점수판
def scoreboard():
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(score), True, WHITE)
    screen.blit(text, (200, 30))

# 최고 점수판
def highestboard():
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(highest_score), True, WHITE)
    screen.blit(text, (10, 30))

def block_speed():
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(speed), True, WHITE)
    screen.blit(text, (screen_width-10, 30))

# 엔딩
def ending():
    global highest_score
    loop = True

    font = pygame.font.SysFont(None, 60)

    # 최고점 갱신
    if highest_score < score:
        highest_score = score
        text = font.render("New Record!", True, WHITE)
    else:
        text = font.render("Game Over!", True, WHITE)

    textRect = text.get_rect()
    textRect.center = (200, 300)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_SPACE:
                    game()
        screen.blit(text, textRect)

        pygame.display.update()
        clock.tick()

# 파이게임 종료
def close():
    pygame.quit()
    sys.exit()

# 조작키 설명
def explain():
    font1 = pygame.font.SysFont(None, 40)
    font2 = pygame.font.SysFont(None, 20)
    text1 = font1.render("Press SPACE to Start!", True, WHITE)
    text2 = font2.render("Press Q to Quit!", True, WHITE)
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = False
                if event.key == pygame.K_q:
                    close()
        
        screen.fill(BLACK)
        screen.blit(text1, (60, 300))
        screen.blit(text2, (150, 500))
        pygame.display.update()
        clock.tick(60)

def pause():
    global paused
    paused = ~paused

def resume():
    global paused
    paused = ~paused

def pausebutton():
    font = pygame.font.SysFont(None, 30)
    text = font.render("Press P to Pause and Resume", True, GREEN)
    # button_rect = pygame.Rect(screen_width - 90, 10, 80, 30)
    # pygame.draw.rect(screen, GREEN, button_rect)
    screen.blit(text, (10, 10))

# 게임 루프
def game():
    global block_width, block_height, speed, score, paused
    loop = True

    # 세팅 초기화
    block_width = 100
    block_height = 10
    speed = 3
    score = 0
    stack = Stack()
    stack.adding()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()    
            if (event.type == pygame.KEYDOWN):
                key = event.key
                if paused and key == pygame.K_p: resume()
                else:
                    if key == pygame.K_SPACE:
                        stack.stacking()
                        stack.adding()
                    if key == pygame.K_q:
                        close()
                    if key == pygame.K_p:
                        pause()
                    if key == pygame.K_u:
                        speedup()
                    if key == pygame.K_d:
                        speeddown()
                    
            
            
        screen.fill(BLACK)

        if not paused:
            stack.move()

        stack.show()
        scoreboard()
        highestboard()
        

        pygame.display.update()
        clock.tick(60)

# 실행
explain()
game()
