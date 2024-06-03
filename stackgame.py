import pygame
import sys

pygame.init()

size = (800, 600)
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.display.flip()

pygame.quit()
sys.exit()
