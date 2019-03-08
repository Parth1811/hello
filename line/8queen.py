import numpy as np

BOARD  = np.zeros((8,8))

def is_safe(BOARD, placing_row, placing_col):
    #Check the row
    for i in range(8):
        if (BOARD[placing_row][i]):
            return False

    #Check the col
    for i in range(8):
        if (BOARD[i][placing_col]):
            return False

    #Check diagonal
    i, j = placing_row, placing_col
    while i > 0 and j > 0:
        if (BOARD[i][j]):
            return False
        else:
            i -= 1
            j -= 1
    i, j = placing_row, placing_col
    while i < 8 and j < 8:
        if (BOARD[i][j]):
            return False
        else:
            i += 1
            j += 1
    i, j = placing_row, placing_col
    while i > 0 and j < 8:
        if (BOARD[i][j]):
            return False
        else:
            i -= 1
            j += 1
    i, j = placing_row, placing_col
    while i < 8 and j > 0:
        if (BOARD[i][j]):
            return False
        else:
            i += 1
            j -= 1

    return True

def place_queen_col(BOARD, placing_col):
    # return True if col is greater than 8
    if (col >= 8)
        return True

    skip = False
    for i in range(8):
        if (BOARD[i][placing_col]==1):
            place_queen_col(BOARD, placing_col=+1)
            skip = True

    if not skip:
        for i in range(8):
            if is_safe(BOARD, i, placing_col):
                board[i][col] = 1
                if place_queen_col(BOARD, placing_col + 1):
                    return True
                board[i][col] = 0;  # BACKTRACK

    return False
