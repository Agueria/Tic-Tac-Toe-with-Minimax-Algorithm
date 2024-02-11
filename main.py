# Initialize a 3x3 tic-tac-toe board with empty spaces
board = [' ' for _ in range(9)]

# Function to check for a winner. It returns True if a player has won.
def check_winner(board, player):
    for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False

# Minimax algorithm to find the best move. It uses recursion and alpha-beta pruning for optimization.
def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
    # Base cases for terminal states
    if check_winner(board, 'X'):
        return -10
    if check_winner(board, 'O'):
        return 10
    if ' ' not in board:
        return 0
    # Maximizing player's turn (O)
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' ' # Undo the move
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    # Minimizing player's turn (X)
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

# Function to find the best move for 'O' and return its index.
def find_best_move(board):
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Function to print the tic-tac-toe board to the console.
def print_board(board):
    for i in range(3):
        print(board[3 * i], '|', board[3 * i + 1], '|', board[3 * i + 2])

# Main game loop function.
def main():
    print("Welcome to Tic-Tac-Toe game")
    print_board(board)
    while ' ' in board:
        player_move = -1
        while player_move not in range(9) or board[player_move] != ' ':
            player_move = int(input("Please make your move (0-8): "))
            if board[player_move] != ' ':
                print("Invalid move, the spot is taken. Try again!")
            else:
                break  # Valid move
        board[player_move] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("X wins!")
            break
        elif ' ' not in board:
            print("Draw!")
            break
        else:
            move = find_best_move(board)
            board[move] = 'O'
            print("Computer's move:")
            print_board(board)
            if check_winner(board, 'O'):
                print("O wins!")
                break

# Call the main function if this file is executed directly.
if __name__ == "__main__":
    main()