import roshen
import pygame
from gui_constants import *


class ChocolateGUI:
    def __init__(self):
        self.chocolate = roshen.Chocolate(6, 8)

        self.CHOCOLATE_CELL_SIZE = 50

        self.CHOCOLATE_WIDTH = self.CHOCOLATE_CELL_SIZE * self.chocolate.m
        self.CHOCOLATE_HEIGHT = self.CHOCOLATE_CELL_SIZE * self.chocolate.n

        self.CHOCOLATE_COORDINATES = (SCREEN_PADDING, SCREEN_PADDING)

        def fill_divisions_coordinates():
            for i in range(1, self.chocolate.n):
                self.horisontalDivisions.append((
                    self.CHOCOLATE_COORDINATES[0] + i * self.CHOCOLATE_CELL_SIZE,
                    self.CHOCOLATE_COORDINATES[1]
                ))

            for j in range(1, self.chocolate.m):
                self.verticalDivisions.append((
                    self.CHOCOLATE_COORDINATES[1] + j * self.CHOCOLATE_CELL_SIZE,
                    self.CHOCOLATE_COORDINATES[0]
                ))

        self.horisontalDivisions = []
        self.verticalDivisions = []

        fill_divisions_coordinates()

    def draw_chocolate(self, surface):
        x = self.CHOCOLATE_COORDINATES[0]
        x_chocolate_end = self.CHOCOLATE_COORDINATES[0] + self.chocolate.m * self.CHOCOLATE_CELL_SIZE

        while x < x_chocolate_end:

            x += self.CHOCOLATE_CELL_SIZE

    def draw_chocolate(self, surface):
        rect = pygame.Rect(
            self.CHOCOLATE_COORDINATES[0],
            self.CHOCOLATE_COORDINATES[1],
            self.CHOCOLATE_WIDTH,
            self.CHOCOLATE_HEIGHT
        )
        CHOCOLATE_COLOR = (150, 75, 0)
        CHOCOLATE_COLOR_DARKER = (60, 30, 0)
        pygame.draw.rect(surface, CHOCOLATE_COLOR, rect)

        for i in range(1, self.chocolate.n):
            y = self.CHOCOLATE_COORDINATES[1] + i * self.CHOCOLATE_CELL_SIZE
            pygame.draw.line(
                surface,
                CHOCOLATE_COLOR_DARKER,
                (self.CHOCOLATE_COORDINATES[0], y),
                (self.CHOCOLATE_COORDINATES[0] + self.CHOCOLATE_WIDTH, y),
                2
            )

        for j in range(1, self.chocolate.m):
            x = self.CHOCOLATE_COORDINATES[0] + j * self.CHOCOLATE_CELL_SIZE
            pygame.draw.line(
                surface,
                CHOCOLATE_COLOR_DARKER,
                (x, self.CHOCOLATE_COORDINATES[1]),
                (x, self.CHOCOLATE_COORDINATES[1] + self.CHOCOLATE_HEIGHT),
                2
            )
