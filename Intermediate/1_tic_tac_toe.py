import random

# Display the board
def display_board(board):
    display = []
    for idx, cell in enumerate(board, 1):
        display.append(str(idx) if cell == ' ' else cell)
    print(f"{display[0]} | {display[1]} | {display[2]}")
    print("---------")
    print(f"{display[3]} | {display[4]} | {display[5]}")
    print("---------")
    print(f"{display[6]} | {display[7]} | {display[8]}")

# Check if a player has won
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combination in winning_combinations:
        if (board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player):
            return True
    return False

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Validate the move
def validate_move(board, position):
    if not position.isdigit():
        return False
    position = int(position) - 1
    if position < 0 or position > 8:
        return False
    if board[position] != ' ':
        return False
    return True

# Get the player's move
def get_human_move(board):
    while True:
        position = input("Enter position (1-9): ")
        if validate_move(board, position):
            return int(position) - 1
        else:
            print("Invalid move. Try again.")

# Get the computer's move
def get_computer_move(board):
    # Check for immediate winning move
    empty_spots = [i for i, cell in enumerate(board) if cell == ' ']
    for spot in empty_spots:
        board[spot] = 'O'
        if check_win(board, 'O'):
            board[spot] = ' '
            return spot
        board[spot] = ' '

    # Check for blocking the player's winning move
    for spot in empty_spots:
        board[spot] = 'X'
        if check_win(board, 'X'):
            board[spot] = ' '
            return spot
        board[spot] = ' '

    # Priority strategy: center, corners, edges
    priority_order = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for spot in priority_order:
        if board[spot] == ' ':
            return spot

    # Fallback to random choice if no spots left (should not happen)
    return random.choice(empty_spots)

def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        print(f"Player {current_player}'s turn.")

        if current_player == 'X':
            move = get_human_move(board)
        else:
            print("Computer's turn...")
            move = get_computer_move(board)

        board[move] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        else:
            if is_board_full(board):
                display_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()