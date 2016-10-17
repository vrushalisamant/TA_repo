from hint_class_helpers.find_matches import find_matches
class Prob8_Part3:
	"""
	Author: Vrushali Samant
	Date: 10/16/2016
	"""

        def check_attempt(self, params):
		
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		hint = ''
		
		matches = find_matches(params)	
		#print "Prob 8 Part 3 matches: ", matches
		try:
                        
			if '*' not in self.attempt:
				hint = 'If the probability of event A is (1/2) is the probability of event B is (1/4), then what is the probability of A and B? Submit the following calculation with the blanks replaced with the appropriate numbers, and then apply this concept to the above problem: (__)*(__).'
				return hint,'(1/2)*(1/3)'

			else:
				return '',''

 	
                except Exception:
                        return '',''
		return '',''

	def get_problems(self):
		self.problem_list = ["PokerConditional/poker_cond3/part3"]
		return self.problem_list

