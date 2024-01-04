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

def play_game():
     board = [[' ' for _ in range(3)] for _ in range(3)]
     current_player = 'X'
     
     while True:
        print_board(board)

        #player move
        row = int(input("picks a row (0,1,2):"))
        col = int(input("pick a column (0,1,2):"))

        #game course
        #empty cell?
        if board[row][col] == ' ':
             board[row][col] = current_player

             #winner?
             if check_winner(board, current_player):
                  print_board(board)
                  print(f"player {current_player} wins")
                  break
             
             #tie?
             if is_board_full(board):
                  print_board(board)
                  print("tie")
                  break
             
             #change player
             current_player = 'O' if current_player =='X' else 'X'
        else:
             print("pick a diffrent cell")
             
if __name__ == "__main__":
    play_game()