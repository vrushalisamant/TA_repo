class Prob4_Part1:
	"""
	Author: Sunil Raiyani
	Date: 10/13/2016
	"""

        def check_attempt(self, params):
		#unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
		
		#print self.answer[7]
		hint=''
		
		try:
			hint='Assume that there are 100 male and 100 female members in the population(since they are equal). Now, use these numbers to find the probabilities used in the equation.'
			
			if len(hint)>0:
                                return hint+' If there are 2% colorblind males, then what is the probability that a person chosen at random is colorblind if we know that the person is male i.e. P(colorblind|male) ?','2/100'
                        else:
                                return '',''
		except Exception:
		        return '',''

	def get_problems(self):
		self.problem_list = ["BayesConditional/BayesColorBlindness/part1"]
		return self.problem_list
