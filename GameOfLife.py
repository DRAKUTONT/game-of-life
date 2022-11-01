import pygame
from pygame.locals import RESIZABLE, QUIT, KEYDOWN, K_SPACE, WINDOWRESIZED
from Cells import Cell
from resource_path import resource_path


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10, grid='r',
                 generation: int = 0, cell_color: tuple = (190, 100, 100), field_color: tuple = (0, 0, 0)) -> None:


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

        self.generation = generation

        self.cell_color = cell_color
        self.field_color = field_color

        self.grid = []
        """Создание поля"""
        if grid == 'r':
            life = 'r'

        else:
            life = False

        for i in range(self.cell_height):
            line = []
            for j in range(self.cell_width):
                try:
                    # при изменении размеров окна
                    cell = Cell(surface=self.screen, coord=(j * self.cell_size, i * self.cell_size),
                                life=grid[i][j].is_alive(), size=self.cell_size, cell_color=self.cell_color,
                                field_color=self.field_color)
                except Exception:
                    cell = Cell(surface=self.screen, coord=(j * self.cell_size, i * self.cell_size),
                                life=life, size=self.cell_size, cell_color=self.cell_color,
                                field_color=self.field_color)

                line.append(cell)
            self.grid.append(line)

    def click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for i, line in enumerate(self.grid):
            for j, elem in enumerate(line):
                elem.click(mouse, click)

    def get_neighbours(self, coord, grid):
        system = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        for i in system:
            if grid[(coord[0] + i[0]) % len(grid)][(coord[1] + i[1]) % len(grid[0])].is_alive():
                count += 1
        return count

    def get_next_generation(self):
        copy_grid = [[j.get_copy() for j in item] for item in self.grid]

        for y, line in enumerate(copy_grid):
            for x, elem in enumerate(line):
                if self.get_neighbours((y, x), copy_grid) == 3:
                    self.grid[y][x].make_live()

                elif self.get_neighbours((y, x), copy_grid) != 2:
                    self.grid[y][x].make_dead()

        # count = 0
        # for i in self.grid:
        #     for j in i:
        #         if j.is_alive():
        #             count += 1
        #
        # self.generation += 1
        # print(f'generation: {self.generation}, count: {count}')

    def draw_grid(self):
        for i, line in enumerate(self.grid):
            for j, elem in enumerate(line):
                if elem.is_alive():
                    elem.draw()
                else:
                    elem.draw_dead()

    def resize_window(self):
        width = self.screen.get_width()
        height = self.screen.get_height()

        self.__init__(width=width, height=height, cell_size=self.cell_size, speed=self.speed, grid=self.grid,
                      generation=self.generation, cell_color=self.cell_color, field_color=self.field_color)

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        icon = pygame.image.load(resource_path('icon.png')).convert()
        pygame.display.set_icon(icon)
        running = True
        stop = False

        while running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        stop = False if stop else True

                if event.type == WINDOWRESIZED:
                    self.resize_window()

            if not stop:
                self.get_next_generation()
                clock.tick(self.speed)
            else:
                clock.tick(360)
            self.draw_grid()
            self.click()
            pygame.display.flip()
        pygame.quit()
