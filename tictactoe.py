"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Khoi tao bang choi moi
    """
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Tra ve nguoi choi co luot tiep theo
    """
    countX = 0;
    countO = 0;
    for row in range (len(board)):
        for col in range(len(board)):
            if board[row][col] == X:
                countX += 1;
            elif board[row][col] == O:
                countO += 1;
    if (countX > countO):
        return O;
    else: return X;



def actions(board):
    """
    Trả về tất cả các nước có thể đi
    """
    possibleAct = set();
    for row in range (len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possibleAct.add((row, col));
    return possibleAct;

def result(board, action):
    """
    Trả về bảng chơi sau khi đi nước (i, j)
    """
    if action not in actions(board):
        raise Exception("Not valid action");
    row, col = action;
    boardClone = copy.deepcopy(board);
    boardClone[row][col] = player(board);
    return boardClone;


def winner(board):
    """
    Tra ve nguoi chien thang neu co
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Tra ve true neu game da ket thuc, False neu game van tiep tuc
    """
    if winner(board) == X: return True;
    if winner(board) == O: return True;

    for row in range (len(board)):
        for col in range (len(board[row])):
            if board[row][col] == EMPTY: 
                return False;
    return True;

def utility(board):
    if winner(board) == X: return 1;
    if winner(board) == O: return -1;
    return 0;

def minimax(board):
    """
    Trả về nước đi tối ưu cho người đi hiện tại
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        point, act = min_value(result(board, action))
        if point > v:
            v = point
            move = action
            if v == 1:
                return v, move
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        point, act = max_value(result(board, action))
        if point < v:
            v = point
            move = action
            if v == -1:
                return v, move
    return v, move