def print_board(board):
    # prints the board in current state of play
        for row in board:
                print(" | ".join(row))
                print("-" * 9)

