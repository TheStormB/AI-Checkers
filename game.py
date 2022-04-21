import pygame
from board import Board
from constants import black, white, green, square_size


class Game:
    def __init__(self, win):
        self._new_init()
        self.win = win

    # I create new init because I didn't wanted to use same thing twice for starting the game and for resetting
    def _new_init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = white
        self.moves = {}

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.moves)
        pygame.display.update()

    def reset(self):
        self._new_init()

    def winner(self):
        self.board.winner()

    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)

        piece = self.board.get(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.moves = self.board.get_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.moves:
            self.board.move(self.selected_piece, row, col)
            skipped = self.moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, green,
                               (col * square_size + square_size // 2, row * square_size + square_size // 2), 15)

    def change_turn(self):
        self.moves = {}
        if self.turn == white:
            self.turn = black
        else:
            self.turn = white


    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()

