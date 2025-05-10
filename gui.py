import pygame
import sys
from gui_constants import *
from chocolate_gui import ChocolateGUI

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("ROSHEN production testing")

clock = pygame.time.Clock()

while True:
    chocolateGui = ChocolateGUI()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    clock.tick(60)
