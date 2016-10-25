# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Problem3Part2:
	"""
	Author: Vrushali Samant
	Date: 10/24/2016
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

		return "What is a component weight?", "It is the probability density of a component in a mixture distribution."

	def get_problems(self):
		self.problem_list = ["CumulativeDistributionFunctions/cdf_norm_uni"]
		return self.problem_list
