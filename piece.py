import pygame
from constants import black, grey, square_size, KING

class Piece():
    padding = 15
    border = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        self.x = square_size * self.col + square_size // 2
        self.y = square_size * self.row + square_size // 2

    def create_king(self):
        self.king = True

    def draw(self, display):
        radius = square_size//2 - self.padding
        pygame.draw.circle(display, grey, (self.x, self.y), radius + self.border)
        pygame.draw.circle(display, self.color, (self.x, self.y), radius)
        if self.king:
            display.blit(KING, (self.x - KING.get_width() // 2, self.y - KING.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.position()

    # for the debugging not so important
    def __repr__(self):
        return str(self.color)