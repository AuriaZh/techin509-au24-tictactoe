import numpy as np


def initialize_board():
    """
    Initializes a 3x3 board using NumPy, filled with empty spaces.
    """
    return np.full((3, 3), " ")


def print_board(board):
    """
    Prints the current state of the game board.

    Args:
        board (ndarray): The current state of the board.
    """
    print("\nCurrent Board:")
    for row in board:
        print("| " + " | ".join(row) + " |")


def check_winner(board, row, col, letter):
    """
    Checks if the current move results in a win.

    Args:
        board (ndarray): The current state of the board.
        row (int): Row index of the move.
        col (int): Column index of the move.
        letter (str): The player's letter ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows
    if all(board[row, :] == letter):
        return True
    # Check columns
    if all(board[:, col] == letter):
        return True
    # Check diagonals
    if row == col and all(np.diag(board) == letter):
        return True
    if row + col == 2 and all(np.diag(np.fliplr(board)) == letter):
        return True
    return False


def is_board_full(board):
    """
    Checks if the board is full (no empty spaces).

    Args:
        board (ndarray): The current state of the board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return not any(board.ravel() == " ")


def get_player_move(board, player):
    """
    Prompts the player to input their move and validates it.

    Args:
        board (ndarray): The current state of the board.
        player (str): The current player ('X' or 'O').

    Returns:
        tuple: The row and column of the valid move (adjusted for 0-based indexing).
    """
    while True:
        user_move = input(f"{player}'s move (row,col), use 1-based indexing (e.g., 1,2): ").strip()
        try:
            # Parse user input
            row, col = map(int, user_move.split(","))
            
            # Convert to 0-based indexing
            row -= 1
            col -= 1

            # Validate the move
            if 0 <= row < 3 and 0 <= col < 3 and board[row, col] == " ":
                return row, col
            else:
                print("Invalid move. Spot is either taken or out of bounds.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter your move as row,col (e.g., 1,2).")


def play_game():
    """
    Manages the Tic Tac Toe game loop and determines the winner.
    """
    board = initialize_board()
    print_board(board)

    current_player = "X"  # Initial player
    while True:
        # Get valid player move
        row, col = get_player_move(board, current_player)

        # Update the board
        board[row, col] = current_player
        print_board(board)

        # Check for a winner
        if check_winner(board, row, col, current_player):
            print(f"Player {current_player} wins!")
            return current_player

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            return None

        # Switch players
        current_player = "O" if current_player == "X" else "X"


def main():
    """
    Main function to run the game with an option to restart.
    """
    print("Welcome to Tic Tac Toe!")
    while True:
        winner = play_game()
        if winner:
            print(f"Congratulations! {winner} is the winner!")
        else:
            print("The game ended in a tie.")

        # Ask if the players want to play again
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
