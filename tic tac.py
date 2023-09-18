# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (a tie)
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    winner = None

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        # Get player's move
        while True:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))

            if row in range(3) and col in range(3) and board[row][col] == " ":
                break
            else:
                print("Invalid move. Try again.")

        board[row][col] = player

        # Check for a win or tie
        if check_win(board, player):
            winner = player
            break
        elif check_tie(board):
            break

        # Switch to the other player
        player = "O" if player == "X" else "X"

    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
