import roshen
from gui_constants import *

class ChocolateGUI:
    def __init__(self):
        self.chocolate = roshen.Chocolate(6, 8)

        CHOCOLATE_CELL_SIZE = 50

        CHOCOLATE_WIDTH = CHOCOLATE_CELL_SIZE * self.chocolate.m
        CHOCOLATE_HEIGHT = CHOCOLATE_CELL_SIZE * self.chocolate.n

        CHOCOLATE_COORDINATES = (SCREEN_PADDING, SCREEN_PADDING)

        def fill_divisions_coordinates():
            for i in range(1, self.chocolate.n):
                self.horisontalDivisions.append((
                    CHOCOLATE_COORDINATES[0] + i * CHOCOLATE_CELL_SIZE,
                    CHOCOLATE_COORDINATES[1]
                ))

            for j in range(1, self.chocolate.m):
                self.verticalDivisions.append((
                    CHOCOLATE_COORDINATES[1] + j * CHOCOLATE_CELL_SIZE,
                    CHOCOLATE_COORDINATES[0]
                ))


        self.horisontalDivisions = []
        self.verticalDivisions = []
