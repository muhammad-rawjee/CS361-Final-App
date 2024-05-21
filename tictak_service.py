import random
import os
import time

def generate_tic_tac_toe_board():
    options = ['X', 'O']
    board = [[random.choice(options) for _ in range(3)] for _ in range(3)]
    return board

def save_board_to_file(board, filename):
    with open(filename, 'w') as file:
        for row in board:
            file.write(' '.join(row) + '\n')

def run_tictak_service():
    while True:
        if os.path.exists('tictak-service.txt'):
            with open('tictak-service.txt', 'r') as file:
                command = file.read().strip()
            if command == 'run':
                board = generate_tic_tac_toe_board()
                save_board_to_file(board, 'tictak-service-output.txt')
            with open('tictak-service.txt', 'w') as file:
                file.write('')  # Clear the command file
            time.sleep(1)  # Allow time for file operations
        time.sleep(1)

if __name__ == "__main__":
    run_tictak_service()
