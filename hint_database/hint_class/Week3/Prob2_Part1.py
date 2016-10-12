# Make sure you name your file with className.py
from hint_class_helpers.find_matches import find_matches
from sets import Set

class Prob2_Part1:
    """
    Author: Shen Ting Ang
    Date: 10/11/2016
    """
    def check_attempt(self, params):
        self.attempt = params['attempt'] #student's attempt
        self.answer = params['answer'] #solution
        self.att_tree = params['att_tree'] #attempt tree
        self.ans_tree = params['ans_tree'] #solution tree
        matches = find_matches(params)
        matching_node = [m[0] for m in matches]

        try:
            if '^' not in self.attempt:
                hint='Missing ^ in the answer.'
                return hint, 'Did you consider the probabilities of the coin flips? '
            #check if the form of the parse tree has the right
            #shape: an operator and two leafs that correspond to
            #the operands

            elif 'C(' not in self.attempt and '!' not in self.attempt:
                hint='Missing choose function in the answer.'
                return hint, 'Did you consider the possible combinations of coin flips?'

            else:
                return "",""

        except Exception:
            return '',''
    def get_problems(self):
        self.problem_list = ["Combinatorics/GrinsteadSnell3.2.18/part1"]
        return self.problem_list
