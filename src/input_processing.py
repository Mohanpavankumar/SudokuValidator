# input_processing.py

def is_valid_input(board):
    """
    Check if the input Sudoku board is valid.
    """
    # Check if the board is a list of lists
    if not isinstance(board, list) or not all(isinstance(row, list) for row in board):
        return False
    
    # Check if the board is 9x9
    if len(board) != 9 or not all(len(row) == 9 for row in board):
        return False
    
    # Check if each cell contains either a digit from 1 to 9 or a dot '.'
    for row in board:
        for cell in row:
            if not isinstance(cell, int) and cell != '.':
                return False
            if isinstance(cell, int) and (cell < 1 or cell > 9):
                return False
    return True

def parse_input(input_str):
    """
    Parse the input string into a 2D list representing the Sudoku board.
    """
    board = []
    lines = input_str.strip().split('\n')
    for line in lines:
        row = []
        for char in line.strip():
            if char.isdigit() and 1 <= int(char) <= 9:
                row.append(int(char))
            elif char == '.':
                row.append('.')
            else:
                return None  # Invalid character encountered
        if len(row) != 9:
            return None  # Incorrect number of cells in a row
        board.append(row)
    if len(board) != 9:
        return None  # Incorrect number of rows
    return board

def read_sudoku_from_file(file_input):
    """
    Read a Sudoku puzzle from a file or file content and parse it into a Sudoku board format.
    Each line in the file represents a row of the Sudoku puzzle, and each digit or dot represents a cell.
    """
    if isinstance(file_input, str):  # If file_input is a file path
        try:
            with open(file_input, 'r') as file:
                input_str = file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_input}' not found.")
            return None
    else:  # If file_input is file content string or StringIO object
        input_str = file_input.getvalue() if hasattr(file_input, 'getvalue') else file_input

    board = []
    lines = input_str.strip().split('\n')
    for line in lines:
        row = []
        for char in line.strip():
            if char.isdigit() and 1 <= int(char) <= 9:
                row.append(int(char))
            elif char == '.':
                row.append('.')
            else:
                return None  # Invalid character encountered
        if len(row) != 9:
            return None  # Incorrect number of cells in a row
        board.append(row)
    if len(board) != 9:
        return None  # Incorrect number of rows
    return board


