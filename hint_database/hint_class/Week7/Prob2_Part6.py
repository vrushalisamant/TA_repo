# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
class Prob2_Part6:
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
				return 'The answer should not contain the variable X. What is the Var(X+Y) where Var(X)=1 and Var(Y)=3?','1+3'
			elif '-' not in self.answer and '-' in self.attempt:
				return 'Var(X-Y) = Var(X)+Var(Y) only when X and Y are independent and identically distributed. What is Var(X-X), then, where Var(X)=1?','0'
			return '', ''
		except Exception:
			return '',''

	def get_problems(self):
		self.problem_list = ["ExpectationVariance/ExpectationVarianceScaling.imd/part6"]
		return self.problem_list
