import copy
import random

class TicTacToe:

    SIZE = 3


    def __init__(self):
        self.board = [[0]*TicTacToe.SIZE for _ in range (TicTacToe.SIZE)]
        self.moves = 0
        self.current_player = 1
        self.game_over = False
        self.terminal_state = 0
    

    def place(self, row, col):
        if self.board[row][col] != 0:
            print("Invalid move")
            return False
        
        self.board[row][col] = self.current_player
        self.moves += 1

        self.current_player = 2 if self.current_player == 1 else 1
        # self.check_win()
        return True
    
    def is_terminal(self) -> bool:
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            return True
        if self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            return True
        if self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            return True
        if self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            return True
        if self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            return True
        if self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return True
        if self.moves == 9:
            return True
        return False
    
    def get_value(self, piece) -> int:
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            if self.board[0][0] == piece:
                return 10
            else:
                return 1
        if self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            if self.board[1][0] == piece:
                return 10
            else:
                return 1
        if self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            if self.board[2][0] == piece:
                return 10
            else:
                return 1
        if self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            if self.board[0][0] == piece:
                return 10
            else:
                return 1
        if self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            if self.board[0][1] == piece:
                return 10
            else:
                return 1
        if self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            if self.board[0][2] == piece:
                return 10
            else:
                return 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            if self.board[0][0] == piece:
                return 10
            else:
                return 1
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            if self.board[0][2] == piece:
                return 10
            else:
                return 1

        if self.moves == 9:
            return 5
  
  
    def simulate_move(self, move: tuple):
        new_board = copy.deepcopy(self)
        new_board.place(move[0], move[1])
        return new_board
    
       
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
        
    def legal_moves(self):
        all_legal_moves = []
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self.board[r][c] == 0:
                    all_legal_moves.append((r, c))
        return all_legal_moves
    
    def __str__(self):
        symbols = {0: " ", 1: "X", 2: "O"}
        rows = []
        for row in self.board:
            rows.append(" " + " | ".join(symbols[cell] for cell in row) + " ")
        return "\n-----------\n".join(rows)
    
    def random_move(self):
        random_move = random.choice(self.legal_moves())
        return self.place(random_move[0], random_move[1])



def main():
    game = TicTacToe()
    game.place(0, 0)
    game.place(0, 1)
    game.place(1, 1)
    game.place(0, 2)
    game.place(2, 2)
    print(game)


if __name__ == "__main__":
    main()