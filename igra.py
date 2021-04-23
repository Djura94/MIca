import copy


def concrete_move_number(board, value):
    return board.count(value)


def inverse_board(board):
    inverse = []
    for position in board:
        if position == "1":
            inverse.append("2")
        elif position == "2":
            inverse.append("1")
        else:
            inverse.append("X")
    return inverse


def isMill(player, board, position1, position2):
    if (board[position1] == player) and (board[position2] == player):
        return True
    return False


def player_have_mill(position, board):
    player = board[position]
    if player != "X":
        return haveBoardMill(position, board, player)
    return False


def nearPositionOnBoard(position):
    positions = [[1, 3], [0, 2, 9], [1, 4], [0, 5, 11], [2, 7, 12], [3, 6], [5, 7, 14], [4, 6], [9, 11],
                 [1, 8, 10, 17], [9, 12], [3, 8, 13, 19], [4, 10, 15, 20], [11, 14], [6, 13, 15, 22], [12, 14],
                 [17, 19], [9, 16, 18], [17, 20], [11, 16, 21], [12, 18, 23], [19, 22], [21, 23, 14], [20, 22]]
    return positions[position]


def haveBoardMill(position, board, player):
    mill = [
        (isMill(player, board, 1, 2) or isMill(player, board, 3, 5)),
        (isMill(player, board, 0, 2) or isMill(player, board, 9, 17)),
        (isMill(player, board, 0, 1) or isMill(player, board, 4, 7)),
        (isMill(player, board, 0, 5) or isMill(player, board, 11, 19)),
        (isMill(player, board, 2, 7) or isMill(player, board, 12, 20)),
        (isMill(player, board, 0, 3) or isMill(player, board, 6, 7)),
        (isMill(player, board, 5, 7) or isMill(player, board, 14, 22)),
        (isMill(player, board, 2, 4) or isMill(player, board, 5, 6)),
        (isMill(player, board, 9, 10) or isMill(player, board, 11, 13)),
        (isMill(player, board, 8, 10) or isMill(player, board, 1, 17)),
        (isMill(player, board, 8, 9) or isMill(player, board, 12, 15)),
        (isMill(player, board, 3, 19) or isMill(player, board, 8, 13)),
        (isMill(player, board, 20, 4) or isMill(player, board, 10, 15)),
        (isMill(player, board, 8, 11) or isMill(player, board, 14, 15)),
        (isMill(player, board, 13, 15) or isMill(player, board, 6, 22)),
        (isMill(player, board, 13, 14) or isMill(player, board, 10, 12)),
        (isMill(player, board, 17, 18) or isMill(player, board, 19, 21)),
        (isMill(player, board, 1, 9) or isMill(player, board, 16, 18)),
        (isMill(player, board, 16, 17) or isMill(player, board, 20, 23)),
        (isMill(player, board, 16, 21) or isMill(player, board, 3, 11)),
        (isMill(player, board, 12, 4) or isMill(player, board, 18, 23)),
        (isMill(player, board, 16, 19) or isMill(player, board, 22, 23)),
        (isMill(player, board, 6, 14) or isMill(player, board, 21, 23)),
        (isMill(player, board, 18, 20) or isMill(player, board, 21, 22)),
    ]
    return mill[position]


def removePiece(board_copy, board_list):
    for piece in range(len(board_copy)):
        if board_copy[piece] == "2":
            if not player_have_mill(piece, board_copy):
                new_board = copy.deepcopy(board_copy)
                new_board[piece] = "X"
                board_list.append(new_board)
    return board_list


def possibleMillNumber(board, player):
    i = 0

    for position in range(len(board)):
        if board[position] == "X":
            if haveBoardMill(position, board, player):
                i += 1
    return i


def phase1(board):
    board_list = []

    for piece in range(len(board)):
        if board[piece] == "X":
            board_copy = copy.deepcopy(board)
            board_copy[piece] = "1"

            if player_have_mill(piece, board_copy):
                board_list = removePiece(board_copy, board_list)
            else:
                board_list.append(board_copy)
    return board_list


def phase2(board):
    board_list = []

    for piece in range(len(board)):
        if board[piece] == "1":
            adjacent_positions = nearPositionOnBoard(piece)

            for position in adjacent_positions:
                if board[position] == "X":
                    board_copy = copy.deepcopy(board)
                    board_copy[piece] = "X"
                    board_copy[position] = "1"

                    if player_have_mill(position, board_copy):
                        board_list = removePiece(board_copy, board_list)
                    else:
                        board_list.append(board_copy)
    return board_list


def phase3(board):
    board_list = []

    for piece in range(len(board)):
        if board[piece] == "1":

            for new_position in range(len(board)):
                if board[new_position] == "X":
                    board_copy = copy.deepcopy(board)

                    board_copy[piece] = "X"
                    board_copy[new_position] = "1"

                    if player_have_mill(new_position, board_copy):
                        board_list = removePiece(board_copy, board_list)
                    else:
                        board_list.append(board_copy)
    return board_list


# U slucaju da jedan od playera ostane sa 3 figure na tabli prelazi se na fazu 3.
def phase23(board):
    if concrete_move_number(board, "1") == 3:
        return phase3(board)
    else:
        return phase2(board)


def heuristicEvaluationPhase23(board):
    nmbrWhite = concrete_move_number(board, "1")
    nmbrBlack = concrete_move_number(board, "2")
    mills = possibleMillNumber(board, "1")

    evaluation = 0

    board_list = phase23(board)
    nmbrBlackMoves = len(board_list)  # Broj poteza koje je odigrao protivnik, nakon svakog naseg poteza

    if nmbrBlack <= 2 or nmbrBlack == 0:
        return float('inf')
    elif nmbrWhite <= 2:
        return float('-inf')
    else:
        return 0


def potentialMills(position, board, player):
    adjacent_positions = nearPositionOnBoard(position)

    for position in adjacent_positions:
        if (board[position] == player) and (not haveBoardMill(position, board, player)):
            return True
    return False


def rowOfPiecesThatCreatePotentialMill(board, player):
    counter = 0

    for piece in range(len(board)):
        if board[piece] == player:
            adjacent_positions = nearPositionOnBoard(piece)
            for position in adjacent_positions:
                if player == "1":
                    if board[position] == "2":
                        board[piece] = "2"
                        if player_have_mill(piece, board):
                            counter += 1
                        board[piece] = player
                else:
                    if board[position] == "1" and potentialMills(position, board, "1"):
                        counter += 1

    return counter


def isPhase3(board):
    countPlayerFigures = 0
    for field in board:
        if field == "1":
            countPlayerFigures += 1
    if countPlayerFigures == 3:
        return True
    else:
        return False


def possibleMove(position1, position2, board):
    if isPhase3(board):
        return True
    else:
        positions = nearPositionOnBoard(position1)
        print(positions)
        if position2 in positions:
            return True
        else:
            return False
