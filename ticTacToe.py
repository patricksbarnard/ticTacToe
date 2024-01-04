def print_board(board):
    # prints the board in current state of play
        for row in board:
                print(" | ".join(row))
                print("-" * 9)

def check_winner(board, player):
    #rows and columns
    for i in range(3):
         if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True 
    #diagonals
    if all(board[i][i] ==player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
         return True
    return False

def is_board_full(board):
     return all(board[i][j] != ' ' for i in range(3) for j in range(3))



