import pygame
import sys

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pygame Test")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.display.flip()

pygame.quit()
sys.exit()
