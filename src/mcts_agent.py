from board import TicTacToe
import random
import math
import copy
import time

class _Node:
    
    def __init__(self, board: "TicTacToe", piece, action=None, parent=None): #board is state, piece is turn
        """
        Only board and piece must be passed. Action and parent are private variables.
        """
        if not action:
            self.current_state = board
        else:
            board_copy = copy.deepcopy(board) #we make a copy of the board and store it to board_copy
            board_copy.place(action[0], action[1]) #we perform the action on the copy of the board
            self.current_state = board_copy
        self.piece = piece
        self.visits = 0 #visits for current node, starts at zero
        self.total_value = 0
        self.children = [] #children stored as empty list. nodes can have either none or as many as they'd like
        self.parent = parent #pointer to parent node, sole purpose of calculating total visits. wait a sec, that's not necessary
        self.action = action
    
    def add_child(self, child: "_Node"):
        self.children.append(child)


class MCTS:

    def __init__(self, board: "TicTacToe", piece):
        self.current_state = board
        self.piece = piece
        self.root_node = _Node(self.current_state, self.piece)
        
    # def random_move(self):
    #     possible_moves = self.board.legal_moves
    #     self.board.place(random.choice(possible_moves)) #what on earth is the purpose of this function? am i stupid?

    def calculate(self, node: "_Node", constant) -> float: #we're assuming 'node' will contain all the necessary values for the calculation # returns UCB1 value for a given node
        if node.visits == 0:
            return math.inf
        else:
            average_value = node.total_value / node.visits
            # parent_visits = 00 #not sure how to get this yet, have to study tree implementations first
            parent_visits = node.parent.visits
            return average_value + constant * math.sqrt(math.log(parent_visits)/node.visits)

    def select(self, node : "_Node") -> _Node: #'traversal'
        if not node.children: #i.e, is node a leaf?
            return node
        else:
            max = -math.inf
            max_node = random.choice(node.children) #this is just in case the ucb value returns negative for all children. not sure if that's a possibility but just in case
            for element in node.children:
                if self.calculate(element, 2) > max: #should i remove the need for a node to be passed to 'calculate' and intead have it return the ucb for the node it's called for? as in, element.calculate(2) instead of the current way
                    max = self.calculate(element, 2)
                    max_node = element
            return self.select(max_node)
        
        
    def node_expansion(self, node: "_Node"):
        if not node.current_state.legal_moves():
            return False
        all_possible_actions = node.current_state.legal_moves()
        for single_action in all_possible_actions:
            node.add_child(_Node(node.current_state, node.piece, single_action, node))
            return True
        
        
    def rollout(self, node: "_Node", piece) -> int:
        if node.visits == 0:
            #perform rollout
            if node.current_state.is_terminal():
                return node.current_state.get_value(piece)
            else:
                return self.rollout(_Node(node.current_state, piece, random.choice(node.current_state.legal_moves()), node), node.piece)
        else:
            #create new state for every action possible
            #check every possible action and create that many children, each child linked to an action
            #node expansion
            if self.node_expansion(node):
                #expansion done
                #after expansion do rollout on random child (all have the same UCB1 value)
                return self.rollout(random.choice(node.children), piece) #guaranteed to rollout since children are newly created meaning they will have a visits value of 0
            else:
                return 0
    
    def backpropagate(self, node: "_Node"): #main function i think
        value = self.rollout(node, node.piece)
        while node:
            node.visits += 1
            node.total_value += value
            node = node.parent
        # current_time = time.time()
        # while time.time() - current_time < 4:
        #     selected = self.select(node)
        #     value = self.rollout(selected, selected.piece)
        #     selected.total_value += value
        #     selected.visits += 1
        #     traversing = node.parent
        #     while traversing:
        #         traversing.total_value += value
        #         traversing.visits += 1
        # max_value = 0
        # max_child = None
        # for element in node.child:
        #     if self.calculate(element, 2) > max_value:
        #         max_value = self.calculate(element, 2)
        #         max_child = element
        # return max_child
        
    def driver(self):
        start_time = time.time()
        while time.time() - start_time < 1:
            chosen_node = self.select(self.root_node)
            self.backpropagate(chosen_node)
        
        max = -math.inf
        best_child = random.choice(self.root_node.children)
        for child in self.root_node.children:
            child_ucb_score = self.calculate(child, 2)
            if child_ucb_score > max:
                max = child_ucb_score
                best_child = child
        
        return best_child.action
    
                
                
        
def main():
    board = TicTacToe()
    agent = MCTS(board, board.current_player)
    while not board.game_over:
        row, col = input("Position: ").split()
        board.place(int(row), int(col))
        print(board)
        agent = MCTS(board, board.current_player)
        action_to_take = agent.driver()
        board.place(action_to_take[0], action_to_take[1])
        print(board)
    print("Game over")
      
if __name__ == "__main__":
    main()
        
        
        