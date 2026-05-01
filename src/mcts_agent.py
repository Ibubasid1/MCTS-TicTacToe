from board import TicTacToe
import random
import math

class _Node:
    
    def __init__(self, board, piece, parent=None): #board is state, piece is turn
        self.current_state = board
        self.piece = piece
        self.visits = 0 #visits for current node, starts at zero
        self.total_value = 0
        self.children = [] #children stored as empty list. nodes can have either none or as many as they'd like
        self.parent = parent #pointer to parent node, sole purpose of calculating total visits. wait a sec, that's not necessary

        self.total_visits = self.visits
        if parent:
            self.total_visits += self.parent.total_visits 
    
    def add_child(self, child: "_Node"):
        self.children.append(child)


class MCTS:

    def __init__(self, board: "TicTacToe", piece):
        self.current_state = board
        self.piece = piece
        self.root_node = _Node(self.current_state, self.piece)

    def calculate(self, node: "_Node", constant) -> float: #we're assuming 'node' will contain all the necessary values for the calculation # returns UCB1 value for a given node
        average_value = node.total_value / node.visits
        # parent_visits = 00 #not sure how to get this yet, have to study tree implementations first
        parent_visits = node.total_visits
        return average_value + constant * ((math.log(parent_visits))/node.visits)^(1/2)

    def select(self, node : "_Node") -> _Node: #'traversal'
        if len(node.children) == 0:
            return node
        else:
            max = 0
            max_node = random.choice(node.children) #this is just in case the ucb value returns negative for all children. not sure if that's a possibility but just in case
            for element in node.children:
                if self.calculate(element, 2) > max: #should i remove the need for a node to be passed to 'calculate' and intead have it return the ucb for the node it's called for? as in, element.calculate(2) instead of the current way
                    max == self.calculate(element, 2)
                    max_node = element
            return self.select(max_node)