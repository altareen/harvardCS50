###
#-------------------------------------------------------------------------------
# tictactoe.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Aug 03, 2021
#
# Venv setup:       python3 -m venv venv
# Venv activation:  source venv/bin/activate
# Run TicTacToe:    python runner.py
# Conclusion:       deactivate
#
# Submission instructions:
# Create a .gitignore file with the folliwng contents:
# __pycache__/
# venv/
# Move inside the folder that contains your project code and execute:
#
# git init
# git remote add origin https://github.com/me50/altareen.git
# git add -A
# git commit -m "Submit my project 0: tictactoe"
# git push origin main:ai50/projects/2020/x/tictactoe
#
##

"""
Tic Tac Toe Player
"""

import copy, math

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
    if sum(row.count(X) for row in board) > sum(row.count(O) for row in board):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possibilities.add((i, j))
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not isinstance(action, tuple) or action[0] > 2 or action[1] > 2:
        raise IndexError
    clone = copy.deepcopy(board)
    clone[action[0]][action[1]] = player(board)
    return clone


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check the rows for a winner
    for row in board:
        if all(map(lambda mark: mark == X, row)):
            return X
        elif all(map(lambda mark: mark == O, row)):
            return O
    # Transpose the board to check the columns for a winner
    clone = copy.deepcopy(board)
    flipped = list(map(list, zip(*clone)))
    for row in flipped:
        if all(map(lambda mark: mark == X, row)):
            return X
        elif all(map(lambda mark: mark == O, row)):
            return O
    # Check the diagonals for a winner
    if [board[0][0]] + [board[1][1]] + [board[2][2]] == [X, X, X] or [board[0][2]] + [board[1][1]] + [board[2][0]] == [X, X, X]:
        return X
    elif [board[0][0]] + [board[1][1]] + [board[2][2]] == [O, O, O] or [board[0][2]] + [board[1][1]] + [board[2][0]] == [O, O, O]:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None or len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        v = float("-inf")
        for action in actions(board):
            current = min_value(result(board, action))
            if current > v:
                v = current
                best_move = action
        return best_move
    elif player(board) == O:
        v = float("inf")
        for action in actions(board):
            current = max_value(result(board, action))
            if current < v:
                v = current
                best_move = action
        return best_move

