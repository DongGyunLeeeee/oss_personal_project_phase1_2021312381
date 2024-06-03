import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stack Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

block_width = 100
block_height = 20
moving_block_y = screen_height // 2
fixed_block = pygame.Rect((screen_width // 2 - block_width // 2, screen_height - block_height), (block_width, block_height))
moving_block = pygame.Rect((screen_width // 2 - block_width // 2, moving_block_y), (block_width, block_height))

block_speed = 5
block_direction = 1

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                overlap = moving_block.clip(fixed_block)
                if overlap.width > 0:
                    fixed_block = overlap
                    moving_block = pygame.Rect((screen_width // 2 - overlap.width // 2, moving_block_y - block_height), (overlap.width, block_height))
                    moving_block_y -= block_height
                else:
                    running = False
    moving_block.x += block_speed * block_direction
    if moving_block.right >= screen_width or moving_block.left <= 0:
        block_direction *= -1

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, fixed_block)
    pygame.draw.rect(screen, RED, moving_block)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
