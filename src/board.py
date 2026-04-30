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

        self.current_player = 2 if self.current_player == 1 else self.current_player = 1
        
        if self.moves == 9:
            self.game_over == True    
       