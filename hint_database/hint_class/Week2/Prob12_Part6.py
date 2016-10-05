# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
from hint_class_helpers.find_matches import find_matches

class Prob12_Part6:
	"""
	Author: Zhen Zhai
	Date: <10-05-2016 00:06>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		matches = find_matches(params)

		if any('R.1' in m for m in matches):
			return "How many different ways to select 6 heads in the H/T sequence of length 9?","C(9,6)"
		return "", ""

	def get_problems(self):
		self.problem_list = ["Combinatorics/coinProblems/part6"]
		return self.problem_list