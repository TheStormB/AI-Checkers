import pygame
from constants import brown, silver, white, black, rows, cols, square_size
from piece import Piece

class Board():
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_king = self.white_king = 0
        self.create_board()


    def squares(self, background):
        background.fill(brown)
        for row in range(rows):
            for col in range(row % 2, cols, 2):
                pygame.draw.rect(background, silver, (row * square_size, col * square_size, square_size, square_size))


    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, black))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, white))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.squares(win)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == rows or row == 0:
            piece.make_king()
            if piece.color == black:
                self.black_king += 1
            else:
                self.white_king += 1

    def get(self, row, col):
        return self.board[row][col]

    def get_moves(self, piece):
        moves = {}
        left = piece.col - 1


