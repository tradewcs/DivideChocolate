import pygame
import sys
from gui_constants import *
from chocolate_gui import ChocolateGUI

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("ROSHEN production testing")

chocolateGui = ChocolateGUI()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")


    screen.fill(SCREEN_BG)
    chocolateGui.draw_chocolate(screen)

    pygame.display.flip()
