import tkinter as tk;
from tkinter import filedialog, messagebox;
from input_processing import read_sudoku_from_file;
from sudoku_validation import is_valid_sudoku;

class SudokuValidatorApp:
    def __init__(self, master):
        self.master = master;
        self.master.title("Sudoku Validator");
        self.master.geometry("300x200");

        self.file_label = tk.Label(self.master, text="Select Sudoku file:")
        self.file_label.pack()

        self.select_button = tk.Button(self.master, text="Select File", command=self.select_file)
        self.select_button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.validate_sudoku(file_path)

    def validate_sudoku(self, file_path):
        sudoku_board = read_sudoku_from_file(file_path)
        if sudoku_board:
            if is_valid_sudoku(sudoku_board):
                messagebox.showinfo("Validation", "Sudoku puzzle is valid!")
            else:
                messagebox.showerror("Validation", "Sudoku puzzle is not valid.")
        else:
            messagebox.showerror("Error", "Failed to read Sudoku puzzle from file.")

def main():
    root = tk.Tk()
    app = SudokuValidatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()