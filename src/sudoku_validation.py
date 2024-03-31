def is_valid_sudoku(board):
    """
    Check if the given Sudoku board is valid.
    """
    # Check rows
    for row in board:
        if not is_valid_row(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_row(column):
            return False

    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
            if not is_valid_row(subgrid):
                return False

    return True


def is_valid_row(row):
    """
    Check if a row (or column, or subgrid) of the Sudoku board is valid.
    """
    seen = set()
    for cell in row:
        if cell != '.' and cell in seen:
            return False
        seen.add(cell)
    return True
