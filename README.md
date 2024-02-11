# Tic-Tac-Toe Game with Minimax Algorithm

This Python script implements a simple console-based Tic-Tac-Toe game that utilizes the Minimax algorithm to calculate the best move for the computer (playing as 'O'). The game allows a human player to compete against the computer in a classic 3x3 Tic-Tac-Toe grid.

## Features

- **Dynamic Board Initialization**: The game board is a 3x3 grid, represented by a list of 9 spaces, initially empty, allowing for dynamic updates as the game progresses.
- **Win Condition Check**: The script includes a function to check if either player has won the game by forming a straight line of their symbol ('X' or 'O') vertically, horizontally, or diagonally.
- **Minimax Algorithm**: An implementation of the Minimax algorithm with alpha-beta pruning to optimize the computer's move calculation, making it a challenging opponent. The algorithm evaluates all possible moves and their outcomes to choose the best move for the computer.
- **Player Input Handling**: The game prompts the human player to input their move by specifying a position number (0-8), with validation to ensure only valid moves are made.
- **Game Flow Management**: The main game loop handles the turn sequence between the human player and the computer, displays the game board after each move, and checks for a win condition or a draw.

## Functions

### `check_winner(board, player)`

- **Parameters**:
  - `board`: The current state of the game board.
  - `player`: The player symbol ('X' or 'O') to check for a winning condition.
- **Returns**: `True` if the specified player has won, `False` otherwise.

### `minimax(board, depth, is_maximizing, alpha, beta)`

- **Purpose**: Implements the Minimax algorithm to find the best move for the computer.
- **Parameters**:
  - `board`: Current game board.
  - `depth`: Current depth of recursion.
  - `is_maximizing`: Boolean indicating if the current move is maximizing or minimizing.
  - `alpha`: Alpha value for alpha-beta pruning.
  - `beta`: Beta value for alpha-beta pruning.
- **Returns**: The score of the board.

### `find_best_move(board)`

- **Purpose**: Determines the best move for the computer by evaluating all possible moves using the Minimax algorithm.
- **Parameters**:
  - `board`: The game board.
- **Returns**: The index of the best move for the computer.

### `print_board(board)`

- **Purpose**: Prints the current state of the game board to the console.
- **Parameters**:
  - `board`: The game board.

### `main()`

- **Purpose**: Contains the main game loop, handling player inputs, game state updates, and displaying the game board. It also checks for win conditions or a draw and announces the game outcome.

## Usage

To play the game, simply run the script in a Python environment. The game will start in the console, and you will be prompted to make the first move by entering a number from 0 to 8. Each number corresponds to a position on the Tic-Tac-Toe grid, starting from the top left corner (0) and ending at the bottom right corner (8).

After each player's turn, the game board will be displayed in the console, showing the current state of the game. The game continues until one player wins by connecting three of their symbols in a line or until all spaces are filled, resulting in a draw.

## Conclusion

This Tic-Tac-Toe game demonstrates the application of the Minimax algorithm in a simple two-player game context. It offers a challenging opponent for the human player and showcases fundamental concepts in game theory and artificial intelligence.
