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

        if row == rows - 1 or row == 0:
            piece.create_king()
            if piece.color == black:
                self.black_king += 1
            else:
                self.white_king += 1

    def get(self, row, col):
        return self.board[row][col]

    def get_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == white or piece.king:
            moves.update(self._diagonal_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._diagonal_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == black or piece.king:
            moves.update(self._diagonal_left(row + 1, min(row + 3, rows), 1, piece.color, left))
            moves.update(self._diagonal_right(row + 1, min(row + 3, rows), 1, piece.color, right))

        return moves

    def _diagonal_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= cols:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)

                    moves.update(self._diagonal_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._diagonal_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        return moves

    def _diagonal_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)

                    moves.update(self._diagonal_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._diagonal_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        return moves

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == white:
                    self.white_left -= 1
                else:
                    self.black_left -= 1

    def winner(self):
        if self.black_left <= 0:
            print("White wins")
        elif self.white_left <= 0:
            print("Black Wins")

        return None


