# Make sure you name your file with className.py
class firstHint:
	"""
	Author: <your name>
	Date: <MM-DD-YYYY HH:MM>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

		if '9' in self.attempt:
			return "1st test hint","1st hint solution"
		return "", ""

	def get_problems(self):
		self.problem_list = ["Combinatorics/p10", "Combinatorics/sw10_2_14", "Poker/q2"]
		return self.problem_list