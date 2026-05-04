from board import TicTacToe
import copy
import math
import random

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
        return not self.children
    
    
    def calculate_ucb1_value(self, constant=2) -> float:
        if self.visits == 0:
            return math.inf
        average_value = self.value/self.visits
        return average_value + constant * math.sqrt(math.log(self.parent.visits)/self.visits)
    

    def get_best_child(self):
        max_ucb1_value = -math.inf
        chosen_child = None
        for child in self.children:
            child_ucb1_value = self.calculate_ucb1_value
            if child_ucb1_value > max_ucb1_value:
                max_ucb1_value = child_ucb1_value
                chosen_child = child
        return chosen_child
    
    
    def expand_node(self) -> bool:
        available_legal_moves = self.current_state.legal_moves()
        if not available_legal_moves:
            return False
        for move in available_legal_moves:
            new_state = self.current_state.simulate_move(move)
            new_child = _Node(new_state, self)
            self.children.append(new_child)
        return True
    
        
    
class MCTS:
    def __init__(self, current_board_layout: "TicTacToe", favored_piece):
        self.board = current_board_layout
        self.root_node = _Node(current_board_layout)
        self.favored_piece = favored_piece
    
    
    def node_selection(self) -> _Node:
        node = self.root_node
        if not node.visits:
            return node
        if not node.children:
            node.expand_node()
        while not node.is_leaf:
            node = node.get_best_child()
        return node
    
    

              