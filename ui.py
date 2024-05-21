import os
import time

def write_command_to_tictak_service():
    with open('tictak-service.txt', 'w') as file:
        file.write('run')

def read_board_from_tictak_service():
    while not os.path.exists('tictak-service-output.txt'):
        time.sleep(1)
    board = []
    with open('tictak-service-output.txt', 'r') as file:
        for line in file:
            board.append(line.strip().split())
    return board

def write_board_to_winner_service(board):
    with open('winner-service.txt', 'w') as file:
        for row in board:
            file.write(' '.join(row) + '\n')

def read_winner_from_winner_service():
    while not os.path.exists('winner-service-output.txt'):
        time.sleep(1)
    with open('winner-service-output.txt', 'r') as file:
        winner = file.read().strip()
    return winner

def main():
    user_input = input("Enter 'run' to generate a tic-tac-toe game and find the winner: ")
    if user_input.lower() == 'run':
        write_command_to_tictak_service()
        time.sleep(1)  # Allow TICTAK service to process the command
        board = read_board_from_tictak_service()
        write_board_to_winner_service(board)
        time.sleep(1)  # Allow Winner service to process the board
        winner = read_winner_from_winner_service()
        print(f'The winner is: {winner}')
    else:
        print("Invalid command. Please enter 'run'.")

if __name__ == "__main__":
    main()

