import os
import time

def load_board_from_file(filename):
    board = []
    with open(filename, 'r') as file:
        for line in file:
            board.append(line.strip().split())
    return board

def check_winner(board):
    # Ensure the board is always a 3x3 grid
    if len(board) != 3 or any(len(row) != 3 for row in board):
        return 'Invalid board'

    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    # If no winner, check for a tie
    for row in board:
        if '' in row:
            return 'No winner'
    
    return 'Tie'

def save_winner_to_file(winner, filename):
    with open(filename, 'w') as file:
        file.write(winner)

def run_winner_service():
    while True:
        if os.path.exists('winner-service.txt') and os.path.getsize('winner-service.txt') > 0:
            board = load_board_from_file('winner-service.txt')
            winner = check_winner(board)
            save_winner_to_file(winner, 'winner-service-output.txt')
            with open('winner-service.txt', 'w') as file:
                file.write('')  # Clear the board file
            time.sleep(1)  # Allow time for file operations
        time.sleep(1)

if __name__ == "__main__":
    run_winner_service()
