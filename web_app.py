from flask import Flask, render_template, request, jsonify
from io import StringIO
from src.input_processing import read_sudoku_from_file
from src.sudoku_validation import is_valid_sudoku

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key for production use

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read file content
            file_content = file.stream.read().decode("utf-8")
            sudoku_board = read_sudoku_from_file(StringIO(file_content))
            if sudoku_board:
                if is_valid_sudoku(sudoku_board):
                    return jsonify({"message": "Sudoku puzzle is valid!", "status": "success"})
                else:
                    return jsonify({"message": "Sudoku puzzle is not valid.", "status": "error"})
            else:
                return jsonify({"message": "Failed to read Sudoku puzzle from file.", "status": "error"})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
