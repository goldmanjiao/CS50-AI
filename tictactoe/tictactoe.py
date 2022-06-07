"""
Tic Tac Toe Player
"""

import math
import copy
from queue import Empty

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #terminal

    X_counter = 0
    O_counter = 0
    for row in board:
        for elem in row:
            if elem == "X":
                X_counter += 1
            elif elem == "O":
                O_counter += 1
    
    if X_counter == O_counter:
        return "X"
    return "O"


    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "X" and board[i][j] != "O":
                available_moves.add((i,j))


    return available_moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)
    board_rep = copy.deepcopy(board)
    board_rep[action[0]][action[1]] = player_turn

    return board_rep


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[0][1] == board[0][2]) and (board[0][0] != None):
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != None:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != None:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != None:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != None:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != None:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[0][2] and board[1][1] != None:
        return board[1][1]
    
    return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in board:
        for elem in row:
            if elem == None:
                return False

    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_play = winner(board)
    if winner_play == "X":
        utility1 = 1
    elif winner_play == "O":
        utility1 = -1
    else:
        utility1 = 0
    return utility1


    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        arr = []
        for action in actions(board):
            arr.append([min_value(result(board,action)),action])
        return sorted(arr,key = lambda x: x[0], reverse=True)[0][1]
    
    elif player(board) == O:
        arr = []
        for action in actions(board):
            arr.append([max_value(result(board,action)),action])
        return sorted(arr,key = lambda x: x[0])[0][1]


    raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v



# board1 = [[O, O, O],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]

# print(player(board1))
# print(actions(board1))

# print(result(board1,(1,2)))
# print(board1[0][0])
# print("winnner is:",winner(board1))
# print(terminal(board1))
# print(utility(board1))