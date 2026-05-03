from board import TicTacToe
import math

class _Node:
    
    def __init__(self, current_board_layout: "TicTacToe", parent=None):
        self.current_state = current_board_layout
        self.visits = 0
        self.value = 0
        self.parent = parent
        self.children = []
        
    def add_child(self, child: "_Node") -> None:
        self.children.append(child)
    
    
class MCTS:
    
    
    def __init__(self, current_board_layout: "TicTacToe", favored_piece):
        self.root_node = _Node(current_board_layout)
        self.favored_piece = favored_piece
        
    
    def calculate(self, node: "_Node", constant) -> float:
        if node.visits == 0:
            return math.inf
        average_value = node.value/node.visits
        parent_visits = node.parent.visits
        return average_value + constant * math.sqrt(math.log(parent_visits)/node.visits)