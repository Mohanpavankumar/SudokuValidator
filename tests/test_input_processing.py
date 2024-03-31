# test_input_processing.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.input_processing import is_valid_input, parse_input

class TestInputProcessing(unittest.TestCase):

    def test_valid_input(self):
        board = [
            [5, 3, '.', '.', 7, '.', '.', '.', '.'],
            [6, '.', '.', 1, 9, 5, '.', '.', '.'],
            ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
            [8, '.', '.', '.', 6, '.', '.', '.', 3],
            [4, '.', '.', 8, '.', 3, '.', '.', 1],
            [7, '.', '.', '.', 2, '.', '.', '.', 6],
            ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
            ['.', '.', '.', 4, 1, 9, '.', '.', 5],
            ['.', '.', '.', '.', 8, '.', '.', 7, 9]
        ]
        self.assertTrue(is_valid_input(board))

    def test_invalid_input(self):
        invalid_board = [
            [5, 3, '.', '.', 7, '.', '.', '.', '.'],
            [6, '.', '.', 1, 9, 5, '.', '.', '.'],
            ['.', 9, 8, '.', '.', '.', '.', 6],  # Missing values in row
            [8, '.', '.', '.', 6, '.', '.', '.', 3],
            [4, '.', '.', 8, '.', 3, '.', '.', 1],
            [7, '.', '.', '.', 2, '.', '.', '.', 6],
            ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
            ['.', '.', '.', 4, 1, 9, '.', '.', 5],
            ['.', '.', '.', '.', 8, '.', '.', 7, 9]
        ]
        self.assertFalse(is_valid_input(invalid_board))

    def test_parse_input(self):
        input_str = (
            "53..7....\n"
            "6..195...\n"
            ".98....6.\n"
            "8...6...3\n"
            "4..8.3..1\n"
            "7...2...6\n"
            ".6....28.\n"
            "...419..5\n"
            "....8..79\n"
        )
        expected_board = [
            [5, 3, '.', '.', 7, '.', '.', '.', '.'],
            [6, '.', '.', 1, 9, 5, '.', '.', '.'],
            ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
            [8, '.', '.', '.', 6, '.', '.', '.', 3],
            [4, '.', '.', 8, '.', 3, '.', '.', 1],
            [7, '.', '.', '.', 2, '.', '.', '.', 6],
            ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
            ['.', '.', '.', 4, 1, 9, '.', '.', 5],
            ['.', '.', '.', '.', 8, '.', '.', 7, 9]
        ]
        self.assertEqual(parse_input(input_str), expected_board)

if __name__ == '__main__':
    unittest.main()