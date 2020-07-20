import sys

import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 400


# class Grid:
# 	lines = 15
# 	columns = 8
#
# 	def draw(self):
# 		block_size = 20  # Set the size of the grid block
# 		for x in range(self.lines):
# 			rect = pygame.Rect(WINDOW_WIDTH /self.columns , WINDOW_HEIGHT / self.lines)
# 			for y in range(self.columns):
# 				rect = pygame.Rect(x * block_size, y * block_size)
# 				pygame.draw.rect(SCREEN, WHITE, rect, 1)

# g = Grid
# g.draw()


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    drawGrid()
    pygame.display.update()


def drawGrid():
    for x in range(int(WINDOW_HEIGHT / 15)):
        for y in range(int(WINDOW_WIDTH / 8)):
            rect = pygame.Rect(x*int(WINDOW_HEIGHT / 15), y, x, y)
            pygame.draw.rect(SCREEN, WHITE, rect)

if __name__ == '__main__':
    main()