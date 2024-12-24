import random

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(str(board[i][j]) if board[i][j] != 0 else ".", end=" ")
        print()

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    def fill_board():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    numbers = random.sample(range(1, 10), 9)
                    for num in numbers:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if fill_board():
                                return True
                            board[row][col] = 0
                    return False
        return True
    fill_board()
    return board

def generate_puzzle(solved_board, difficulty=40):
    puzzle = [row[:] for row in solved_board]
    count = difficulty
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            count -= 1
    return puzzle

def get_user_input(board):
    while True:
        try:
            row = int(input("Enter row (1-9) or '0' to give up: ")) - 1
            if row == -1:
                return "give up"
            col = int(input("Enter column (1-9): ")) - 1
            num = int(input("Enter number (1-9): "))
            if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                if board[row][col] == 0:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        return board
                    else:
                        print("Invalid move! Try again.")
                else:
                    print("Cell is already filled! Try a different empty cell.")
            else:
                print("Invalid input. Please enter valid row, column, and number.")
        except ValueError:
            print("Please enter valid integer values.")

solved_board = generate_sudoku()
sudoku_puzzle = generate_puzzle(solved_board, difficulty=40)
print("Generated Sudoku Puzzle:")
print_board(sudoku_puzzle)

while True:
    user_input = get_user_input(sudoku_puzzle)
    if user_input == "give up":
        print("\n nanda! You gave up? mattaku ! sore wa solved puzzle desu")
        print_board(solved_board)
        break
    print("\nCurrent Sudoku Puzzle:")
    print_board(sudoku_puzzle)
    if all(board != 0 for row in sudoku_puzzle for board in row):
        print("\n gambare gambre! you did it ! you completed the game !")
        break
