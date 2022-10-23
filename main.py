from GameOfLife import GameOfLife


def main(screen_w: int = 1368, screen_h: int = 762, cell_size: int = 10, speed: int = 10):
    game = GameOfLife(width=screen_w, height=screen_h, cell_size=cell_size, speed=speed)
    game.run()


if __name__ == '__main__':
    main()
