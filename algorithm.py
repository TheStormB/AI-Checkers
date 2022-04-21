from copy import deepcopy
import pygame
from constants import black, white, green

def min_max(position, depth, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluation(), position

    if max_player:
        max_evaluation = float('-inf')
        best_move = None
        for move in get_moves(position, white, game):
            evaluation = min_max(move, depth - 1, False, game)[0]
            max_evaluation = max(max_evaluation, evaluation)
            if max_evaluation == evaluation:
                best_move = move
        return max_evaluation, best_move
    else:
        min_evaluation = float('inf')
        best_move = None
        for move in get_moves(position, black, game):
            evaluation = min_max(move, depth - 1, False, game)[0]
            min_evaluation = min(min_evaluation, evaluation)
            if min_evaluation == evaluation:
                best_move = move
        return min_evaluation, best_move


def get_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get(piece.row, piece.col)
            new_board = move_simulation(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def move_simulation(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def draw_moves(game, board, piece):
    valid_moves = board.get_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, green, (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)
