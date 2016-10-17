# Make sure you name your file with className.py

from sets import Set

class Prob12_Part1:
	"""
	Author: Geovonni Najera
	Date: 10-17-2016
	"""

        def check_attempt(self, params):
                #unpack params
                self.attempt = params['attempt'] #student's attempt
                self.answer = params['answer'] #solution
                self.att_tree = params['att_tree'] #attempt tree
                self.ans_tree = params['ans_tree'] #solution tree

                return 'Recall what the defination for conditional probality is, in terms of intersections'+
                       ' and sets',''

	def get_problems(self):
		self.problem_list = ["BayesConditional/BayesBurglary"]
		return self.problem_list
