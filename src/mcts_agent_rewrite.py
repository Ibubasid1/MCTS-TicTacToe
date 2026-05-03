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
    
    
    @property
    def is_leaf(self) -> bool:
        return not self.children\
    
    
    @property
    def calculate_ucb1_value(self, constant=2) -> float:
        if self.visits == 0:
            return math.inf
        average_value = self.value/self.visits
        return average_value + constant * math.sqrt(math.log(self.parent.visits)/self.visits)
    
    
    @property 
    def get_best_child(self):
        max_UCB1_value = -math.inf
        chosen_child = None
        for child in self.children:
            child_UCB1_value = self.calcul
    
    
    
class MCTS:
    
    
    def __init__(self, current_board_layout: "TicTacToe", favored_piece):
        self.root_node = _Node(current_board_layout)
        self.favored_piece = favored_piece
    
    

                        