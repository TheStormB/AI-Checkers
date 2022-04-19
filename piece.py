import pygame
from constants import black, grey, square_size

class Piece():
    padding = 15
    border = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.piece = False
        self.x = 0
        self.y = 0
        self.position()

        if self.color == black:
            self.direction = -1
        else:
            self.direction = 1

    def position(self):
        self.x = square_size * self.col + square_size // 2
        self.y = square_size * self.row + square_size // 2

    def create_piece(self):
        self.piece = True

    def draw(self, win):
        radius = square_size//2 - self.padding
        pygame.draw.circle(win, grey, (self.x, self.y), radius + self.border)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)


    def move(self, row, col):
        self.row = row
        self.col = col
        self.position()

    # for the debugging not so important
    def __repr__(self):
        return str(self.color)