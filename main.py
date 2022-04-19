import pygame
from constants import width, height, square_size
from game import Game
fps = 60
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Checkers')


def get_position(position):
    x, y = position
    row = y // square_size
    col = x // square_size
    return row, col


def main():
    run = True
    # limiting fps
    clock = pygame.time.Clock()
    game = Game(display)

    while run:
        clock.tick(fps)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position(pos)

        game.update()

    pygame.quit()


if __name__ == '__main__':
    main()
