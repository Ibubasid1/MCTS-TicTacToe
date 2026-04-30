class TicTacToe:

    SIZE = 3


    def __init__(self):
        self.board = [[0]*TicTacToe.SIZE for _ in range (TicTacToe.SIZE)]
        self.moves = 0
        self.current_player = 1
        self.game_over = False
    

    def place(self, row, col):
        if self.board[row][col] != 0:
            print("Invalid move")
            return False
        
        self.board[row][col] = self.current_player
        self.moves += 1

        self.current_player = 2 if self.current_player == 1 else 1
        return True
  
       
    def check_win(self):
        
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            if self.board[0][0] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return
        if self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            if self.board[1][0] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return
        if self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            if self.board[2][0] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return
        if self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            if self.board[0][0] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return
        if self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            if self.board[0][1] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return
        if self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            if self.board[0][2] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            if self.board[0][0] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            if self.board[0][2] == 1:
                print("X wins")
            else:
                print("O wins")
            self.game_over = True
            return

        if self.moves == 9:
            self.game_over = True
            print("Draw")
            return