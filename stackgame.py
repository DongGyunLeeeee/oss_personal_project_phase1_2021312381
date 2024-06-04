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
speed = 3

# 점수
score = 0
highest_score = 0
clock = pygame.time.Clock()

class Block:
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
        if self.x > screen_width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1

class Stack:
    def __init__(self):
        self.stack = []
        self.initSize = 20
        for i in range(self.initSize):
            newBlock = Block(150, 590 - i * 10, RED, 0)
            self.stack.append(newBlock)

    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    def adding(self):
        newBlock = Block(0, 390, RED, speed)
        self.initSize += 1
        self.stack.append(newBlock)

    def stacking(self):
        global block_width, score
        lowerIndex = self.initSize - 2
        upperIndex = self.initSize - 1

        lowerBlock = self.stack[lowerIndex]
        upperBlock = self.stack[upperIndex]
        if upperBlock.x <= lowerBlock.x and not (upperBlock.x + upperBlock.w < lowerBlock.x):
            self.stack[upperIndex].w = self.stack[upperIndex].x + self.stack[upperIndex].w - lowerBlock.x
            self.stack[upperIndex].x = lowerBlock.x
            if self.stack[upperIndex].w > lowerBlock.w:
                self.stack[upperIndex].w = lowerBlock.w
            self.stack[upperIndex].speed = 0
            score += 1
        elif lowerBlock.x <= upperBlock.x <= lowerBlock.x + lowerBlock.w:
            self.stack[upperIndex].w = lowerBlock.x + lowerBlock.w - upperBlock.x
            self.stack[upperIndex].speed = 0
            score += 1
        else:
            close()
        for i in range(self.initSize):
            self.stack[i].y += 10

        block_width = self.stack[upperIndex].w




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
    global block_width, block_height, speed, score
    loop = True

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stack.stacking()
                    stack.adding()
                if event.key == pygame.K_q:
                    close()
        
        screen.fill(BLACK)
        stack.move()
        stack.show()
        scoreboard()
        highestboard()
        pygame.display.update()
        clock.tick(60)

game()
