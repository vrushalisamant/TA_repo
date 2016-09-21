class className:

	def check_attempt(self, params):
		self.attempt = params['attempt']
		self.answer = params['answer']
		self.att_tree = params['att_tree']
		self.ans_tree = params['ans_tree']
		if (condition):
			return "hint"
		return ""

	def get_problems(self):
		self.problem_list = [(problemID, partID), (problemID2, partID2)]
		return self.problem_list