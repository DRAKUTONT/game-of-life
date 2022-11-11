import pygame
from random import choice
from typing import Union


class Cell:
    def __init__(self, surface, coord: tuple[int, int], life: Union[str, bool], size: int = 10,
                 cell_color: tuple = (190, 100, 100), field_color: tuple = (0, 0, 0)):
        self.surface = surface
        self.coord = coord
        self.life = life if isinstance(life, bool) else self.random_life()
        self.size = size
        self.rect = pygame.Rect(*coord, size, size)

        self.cell_color = cell_color
        self.field_color = field_color

    def draw(self) -> None:
        pygame.draw.rect(self.surface, self.cell_color, self.rect)

    def draw_dead(self):
        pygame.draw.rect(self.surface, self.field_color, self.rect)

    def is_alive(self) -> bool:
        return self.life

    def make_live(self):
        self.life = True

    def make_dead(self):
        self.life = False

    def click(self, mouse: tuple[int, int], click: tuple):
        if self.rect.bottomleft[0] < mouse[0] < self.rect.bottomright[0] and self.rect.bottomleft[1] > mouse[1] > \
                self.rect.topleft[1]:
            if click[0]:
                self.life = True
            if click[2]:
                self.life = False

    def random_life(self):
        life = choice((False, False, False, False, False, False, True))
        return life

    def get_copy(self):
        return Cell(self.surface, self.coord, self.life, self.size)
