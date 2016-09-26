# Make sure you name your file with className.py
class Printout:
	"""
	Author: Yoav Freund
	Date: 9/25/2016
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

                print 'attempt_tree=\n',self.att_tree
                print 'answer tree=\n',self.ans_tree
		return "", ""

	def get_problems(self):
		self.problem_list = []
		return self.problem_list
