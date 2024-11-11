import random

def print_board(board):
    """Print the Sudoku board with 3x3 grid separation."""
    for i in range(9):
        # Print row with grid separation
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Add a separator line between 3x3 grids
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Add vertical grid separator
            print(str(board[i][j]) if board[i][j] != 0 else ".", end=" ")  # Print number or '.' for empty
        print()  # Newline at the end of each row

def is_valid(board, row, col, num):
    """Check if it's valid to place the number at the position (row, col)."""
    # Check the row
    if num in board[row]:
        return False
    
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check the 3x3 box
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty space
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Try this number
                        
                        if solve(board):
                            return True
                        
                        board[row][col] = 0  # Reset if the number didn't work
                return False  # If no number is valid, return False
    return True  # If all cells are filled correctly

def generate_sudoku():
    """Generate a random solved Sudoku board."""
    board = [[0 for _ in range(9)] for _ in range(9)]

    def fill_board():
        """Helper function to fill the board using backtracking."""
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    numbers = random.sample(range(1, 10), 9)  # Randomize order of 1-9
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
    """Generate a Sudoku puzzle by removing values from a solved board."""
    puzzle = [row[:] for row in solved_board]  # Make a copy of the solved board
    count = difficulty  # Number of cells to remove
    
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            count -= 1
    
    return puzzle

def get_user_input(board):
    """Get user input to solve the Sudoku puzzle."""
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

# Generate a fully solved Sudoku board
solved_board = generate_sudoku()

# Generate a Sudoku puzzle with removed numbers
sudoku_puzzle = generate_puzzle(solved_board, difficulty=40)  # Difficulty: 40 means 40 empty cells

# Print the initial (unsolved) Sudoku puzzle
print("Generated Sudoku Puzzle:")
print_board(sudoku_puzzle)

# Game loop
while True:
    # Prompt user for input to solve the puzzle
    user_input = get_user_input(sudoku_puzzle)
    
    if user_input == "give up":
        print("\nYou gave up. Here's the solved puzzle:")
        print_board(solved_board)
        break
    
    # Print the updated board
    print("\nCurrent Sudoku Puzzle:")
    print_board(sudoku_puzzle)
    
    # Check if the puzzle is solved
    if all(board != 0 for row in sudoku_puzzle for board in row):
        print("\nCongratulations! You solved the puzzle!")
        break
