# 8 queens
# Print all the ways to arrange 8 queens on an 8x8 chessboard so that none are under attack.

# Assumptions:
# - Print the actual visual representation
# - Can change board size later
# - Standard chess rules

# Questions:
# - Rotations or reflections?
# - Do we want to find all configurations, or just the first one?

import numpy as np

BOARD_SIZE = 8
NO_QUEEN = 0
UNDER_ATTACK = 1

# Feedback: This is overly complicated by initializing the chessboard.
# Instead, I should have simply just checked placement only
# because I don't need to render the chessboard until the very end.
# To check the diagonals, if the absolute distance between columns of two
# different squares is equal to the absolute distance between rows, then they're
# on the same diagonal.

def set_under_attack(row, col, chessboard):
    chessboard[row, col] = UNDER_ATTACK
    chessboard[row] = UNDER_ATTACK
    chessboard[:, col] = UNDER_ATTACK

    for i in range(BOARD_SIZE):
        if row-i < 0 or col-i < 0:
            break
        chessboard[row-i, col-i] = UNDER_ATTACK

    for i in range(BOARD_SIZE):
        if row+i > BOARD_SIZE-1 or col-i < 0:
            break
        chessboard[row+i, col-i] = UNDER_ATTACK


    for i in range(BOARD_SIZE):
        if row-i < 0 or col+i > BOARD_SIZE-1:
            break
        chessboard[row-i, col+i] = UNDER_ATTACK


    for i in range(BOARD_SIZE):
        if row+i > BOARD_SIZE-1 or col+i > BOARD_SIZE-1:
            break
        chessboard[row+i, col+i] = UNDER_ATTACK

def eight_queens(col_idx=0, all_queens=[], queens=[], chessboard=None):
    if chessboard is None:
        # Initialize empty chessboard
        # Indexing is column, then row
        chessboard = np.zeros((BOARD_SIZE, BOARD_SIZE))

    # If this is the last row, then return the queens
    if col_idx > BOARD_SIZE-1:
        # print("FOUND ALL QUEENS")
        return queens

    # If the entire column is under attack, then this layout is invalid
    if chessboard[:, col_idx].sum() == UNDER_ATTACK * BOARD_SIZE:
        # print("Nowhere to place queens in this column")
        return False

    # Place a queen at the first available row
    row_idx = 0
    while row_idx < BOARD_SIZE:
        if chessboard[row_idx, col_idx] == NO_QUEEN:
            old_queens = queens.copy()
            old_chessboard = chessboard.copy()
            set_under_attack(row_idx, col_idx, chessboard)
            queens.append((row_idx, col_idx))
            # print(f"Placed a queen at {(row_idx, col_idx)}")
            # print(f"Queens is {queens}")
            # print(chessboard)

            # Recurse to the next column
            found_queens = eight_queens(col_idx + 1, all_queens, queens, chessboard)
            if found_queens:
                # If the recursion was successful, then return the queens
                if col_idx == BOARD_SIZE-1:
                    all_queens.append(found_queens)
                elif col_idx == 0:
                    queens = []
                    chessboard = np.zeros((BOARD_SIZE, BOARD_SIZE))
                    chessboard[0:row_idx, 0] = UNDER_ATTACK
                else:
                    return found_queens
            # Otherwise, reset the queens, and try placing a queen at the next
            # available row.
            else:
                queens = old_queens
                chessboard = old_chessboard
                # print("Resetting chessboard")
                # print(f"Queens is {queens}")
                # print(chessboard)

        row_idx += 1

    # If we got to the last row, and still haven't placed any queens,
    # then it is impossible to solve this subproblem
    # We will never get here during normal reursion because we first checked
    # if the entire column is under attack
    if col_idx == 0:
        return all_queens
    return False

print()
all_solutions = eight_queens()
print(all_solutions)

for solution in all_solutions:
    print()
    board = [['▢' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for queen in solution:
        board[queen[0]][queen[1]] = '♕'
    print('\n'.join([''.join(row) for row in board]))

print(f"Num solutions: {len(all_solutions)}")
