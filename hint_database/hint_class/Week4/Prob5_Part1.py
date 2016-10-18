class Prob5_Part1:
	"""
	Author: Chang Qiu
	Date: 10/17/2016
	"""

	def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
		
		try:
			if not '^' in self.attempt:
				hint = 'You have 2 ranks, and each rank has 4 suits.'

			elif 'C' in self.attempt:

				hint = 'We do not need combinations for this part.'

			elif '+' in self.attempt:
				
				hint = 'Should you add different parts of your expression?'

			elif '-' in self.attempt:

				hint = 'Should you do subtraction?'

			elif '!' in self.attempt:

				hint = 'Should you do factorial?'

			if len(hint) > 0:

				return hint +' 2, 4, 5, 6 are already shown, so what else do you need to form a straight? Also remember order does not matter.'
			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond2_1/part1"]
		return self.problem_list