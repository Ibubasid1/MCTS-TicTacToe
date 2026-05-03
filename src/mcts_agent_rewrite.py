from board import TicTacToe

class _Node:
    
    def __init__(self, current_board_layout: "TicTacToe", parent=None):
        self.current_state = current_board_layout
        self.visits = 0
        self.value = 0
        self.parent = parent
        self.children = []
        
    def add_child(self, child: "_Node"):
        self.children.append(child)
    
    
