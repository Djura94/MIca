from copy import deepcopy

from igra import *


class evaluator:
    def __init__(self):
        self.evaluator = 0
        self.board = []


def minimax(board, depth, player, alfa, beta, phase1Boll, heuristic):
    result = evaluator()
    if player:
        player_sign = "1"
    else:
        player_sign = "2"
    if depth != 0:

        possible_moves = get_possible_moves(board, player_sign, phase1Boll)
        for move in possible_moves:

            current_state = minimax(move, depth - 1, not player, alfa, beta, phase1Boll, heuristic)
            if current_state.evaluator > alfa and player:
                alfa = current_state.evaluator
                result.board = move

            if current_state.evaluator < beta and not player:
                beta = current_state.evaluator
                result.board = move

        if player:
            result.evaluator = alfa
        else:
            result.evaluator = beta

    else:
        if player:
            result.evaluator = heuristic(board, phase1Boll)

        else:
            result.evaluator = heuristic(inverse_board(board), phase1Boll)

    return result


def get_possible_moves(board, player_sign, state):
    boards = []
    if state:
        for position in range(len(board)):
            copy_board = deepcopy(board)
            if copy_board[position] == "X":
                copy_board[position] = player_sign
                if player_have_mill(position, copy_board):
                    boards = removePiece(copy_board, boards)
                else:
                    boards.append(copy_board)
    elif get_game_state(board, player_sign) == 2:
        for position in range(len(board)):
            if board[position] == player_sign:
                near_positions = get_near_positions(position)
                for near_position in near_positions:
                    if board[near_position] == "X":
                        copy_board = deepcopy(board)
                        copy_board[position] = "X"
                        copy_board[near_position] = player_sign
                        if player_have_mill(near_position, copy_board):
                            boards = removePiece(copy_board, boards)
                        else:
                            boards.append(copy_board)
    elif get_game_state(board, player_sign) == 3:
        for position in range(len(board)):
            if board[position] == player_sign:
                copy_board = deepcopy(board)
                for new_position in range(len(board)):
                    if copy_board[new_position] == "X":
                        copy_board[position] = "X"
                        copy_board[new_position] = player_sign
                        if player_have_mill(new_position, copy_board):
                            boards = removePiece(copy_board, boards)
                        else:
                            boards.append(copy_board)
    return boards


def get_game_state(board, player_sign):
    counter = 0
    for position in range(len(board)):
        if board[position] == player_sign:
            counter += 1
    if counter > 3:
        return 2
    else:
        return 3


def get_near_positions(position):
    near_positions = [[1, 3], [0, 2, 9], [1, 4], [0, 5, 11], [2, 7, 12], [3, 6], [5, 7, 14], [4, 6], [9, 11],
                      [1, 8, 10, 17], [9, 12], [3, 8, 13, 19], [4, 10, 15, 20], [11, 14], [6, 13, 15, 22], [12, 14],
                      [17, 19], [9, 16, 18], [17, 20], [11, 16, 21], [12, 18, 23], [19, 22], [21, 23, 14], [20, 22]]
    return near_positions[position]
