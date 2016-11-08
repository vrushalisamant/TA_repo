# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob2_Part1:
	"""
	Author: Vrushali Samant 
	Date: <11-07-2016 18:50>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		try:
			if 'x' in self.attempt or 'X' in self.attempt:
				return 'The answer should not contain the variable X. What is the E(2X-3Y) where E(X)=1 and E(Y)=3?','2*1-3*3'
			elif '-' in self.answer and '-' not in self.attempt:
				return 'Remember that E(aX-Y) = E(aX) + E(-Y) = aE(X) - E(Y). Knowing this, what is E(2X-3Y) where E(X)=1 and E(Y)=3?','2*1-3*3'
			return '', ''
		except Exception:
			return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/ExpectationVarianceScaling.imd/part1","ExpectationVariance/ExpectationVarianceScaling.imd/part2", "ExpectationVariance/ExpectationVarianceScaling.imd/part3"]
		return self.problem_list
