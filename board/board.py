from board.grid import WINDOW_WIDTH, WINDOW_HEIGHT, Grid, WHITE
import pygame

global SCREEN, CLOCK


def drawGrid():
    blockSize = 20  # Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x * blockSize, y * blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


class Board:
    grid = Grid()

