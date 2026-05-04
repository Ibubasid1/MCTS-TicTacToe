from board import TicTacToe
import copy
import math
import random
import time

class _Node:
    def __init__(self, current_board_layout: "TicTacToe", parent=None, move=None):
        self.current_state = current_board_layout
        self.visits = 0
        self.value = 0
        self.parent = parent
        self.move = move
        self.children = []
        
        
    def add_child(self, child: "_Node") -> None:
        self.children.append(child)
    
    
    @property
    def is_leaf(self) -> bool:
        return not self.children
    
    
    def calculate_ucb1_value(self, constant=2) -> float:
        if self.visits == 0 or not self.parent:
            return math.inf
        average_value = self.value/self.visits
        return average_value + constant * math.sqrt(math.log(self.parent.visits)/self.visits)
    

    def get_best_child(self):
        max_ucb1_value = -math.inf
        chosen_child = None
        for child in self.children:
            child_ucb1_value = self.calculate_ucb1_value()
            if child_ucb1_value > max_ucb1_value:
                max_ucb1_value = child_ucb1_value
                chosen_child = child
        return chosen_child
    
    
    def most_loved_child(self):
        most_visited = random.choice(self.children)
        for child in self.children:
            if child.visits > most_visited.visits:
                most_visited = child
        return most_visited
    
    
    def expand_node(self) -> bool:
        available_legal_moves = self.current_state.legal_moves()
        if not available_legal_moves:
            return False
        for move in available_legal_moves:
            new_state = self.current_state.simulate_move(move)
            new_child = _Node(new_state, self, move)
            self.children.append(new_child)
        return True      
    
        
    
class MCTS:
    def __init__(self, current_board_layout: "TicTacToe", favored_piece):
        self.board = current_board_layout
        self.root_node = _Node(current_board_layout)
        self.favored_piece = favored_piece
    
    
    def node_selection(self) -> _Node:
        node = self.root_node
        while not node.is_leaf:
            node = node.get_best_child()
        return node
    
    
    def simulation(self, node: "_Node"):
        state = copy.deepcopy(node.current_state)
        while True:
            if state.is_terminal():
                return state.get_value(self.favored_piece)
            state = state.simulate_move(state.random_move())
    
    
    def backpropagate(self, node: "_Node", value):
        current_node = node
        while True:
            current_node.visits += 1
            current_node.value += value
            if not current_node.parent:
                break
            current_node = current_node.parent
            
    
    def get_best_move(self):
        current_time = time.time()
        while time.time() - current_time < 1:
            node = self.node_selection()
            if not node.current_state.is_terminal():
                if node.visits:
                    node.expand_node()
                    node = random.choice(node.children) 
            value = self.simulation(node)
            self.backpropagate(node, value)
        most_visited_child = self.root_node.most_loved_child()
        return most_visited_child.move
        
            
            
def main():
    board = TicTacToe()
    board.place(0, 0)
    board.place(0, 1)
    board.place(0, 2)
    board.place(1, 0)
    board.place(2, 0)
    # board.place(1, 1)
    # board.place(1, 2)
    # board.place(2, 1)
    # board.place(2, 2)
    print(board)
    agent = MCTS(board, 1)
    move = agent.get_best_move()
    board.place(move[0], move[1])
    # print(agent.simulation())
    print(board)
    
if __name__ == "__main__":
    main()              