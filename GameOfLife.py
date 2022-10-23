import pygame
from pygame.locals import *
import random
from copy import deepcopy
from Cells import Cell

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_size = width, height

        self.screen = pygame.display.set_mode(self.screen_size, RESIZABLE)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = speed

        self.generation = 0

        self.grid = [
            [Cell(surface=self.screen, coord=(j * self.cell_size, i * self.cell_size), life='r', size=self.cell_size)
             for j in range(self.cell_width)] for i in
            range(self.cell_height)]

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for i, item in enumerate(self.grid):
            for j, jtem in enumerate(item):
                jtem.click(mouse, click)

    def get_neighbours(self, coord):
        system = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        for i in system:
            if self.new_greed[(coord[0] + i[0]) % len(self.new_greed)][(coord[1] + i[1]) % len(self.new_greed[0])].is_alive():
                count += 1
        return count

    def get_next_generation(self):
        self.new_greed = [[j.get_copy() for j in item] for item in self.grid]

        for y, item in enumerate(self.new_greed):
            for x, jtem in enumerate(item):
                if self.get_neighbours((y, x)) == 3:
                    self.grid[y][x].make_live()

                elif self.get_neighbours((y, x)) != 2:
                    self.grid[y][x].make_dead()

        count = 0
        for i in self.grid:
            for j in i:
                if j.is_alive():
                    count += 1

        self.generation += 1
        print(f'generation: {self.generation}, count: {count}')

    def draw_grid(self):
        for i, item in enumerate(self.grid):
            for j, jtem in enumerate(item):
                if jtem.is_alive():
                    jtem.draw()

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        running = True

        while running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        stop = False
                        while not stop:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    running = False

                                if event.type == KEYDOWN:
                                    if event.key == K_SPACE:
                                        stop = True

            self.get_next_generation()
            self.draw_lines()
            self.draw_grid()
            self.click()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
