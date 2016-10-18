class Prob5_Part2:
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
			if not 'C(' in self.attempt:
				hint = 'How do you pick 2 cards from a deck?'
				return hint + 'if you are going to pick 3 cards from a 10-card deck, how many combinations are there?', 'C(10,3)'

			elif not '-' in self.attempt:

				hint = 'What is the complement of at least a 3 shows in turn and river?'
				return hint + ' what is the complement of at least one?', 'None'

			elif 'P(' in self.attempt:

				hint = 'Does the order of the selected cards matter?'
				return hint + 'if you are going to pick 3 cards from a 10-card deck, how many combinations are there?', 'C(10,3)'

			elif '+' in self.attempt:
				
				hint = 'Should you add different parts of your expression?'
				return hint + 'if you are going to pick 3 cards from a 10-card deck, how many combinations are there?', 'C(10,3)'

			elif '!' in self.attempt:

				hint = 'Should you do factorial?'
				return hint + 'if you are going to pick 3 cards from a 10-card deck, how many combinations are there?', 'C(10,3)'

			elif '*' in self.attempt:

				hint = 'Should you multiply different parts of your expression?'
				return hint + 'if you are going to pick 3 cards from a 10-card deck, how many combinations are there?', 'C(10,3)'

			if len(hint) > 0:

				return hint +' How do you pick 2 cards from a 47-card(52 - 5) deck?', 'C(47,2)'
			else:

				return '',''

		except Exception:

			return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond2_1/part2"]
		return self.problem_list