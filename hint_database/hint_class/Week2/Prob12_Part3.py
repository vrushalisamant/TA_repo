        # Make sure you name your file with className.py

from sets import Set

class Prob12_Part3:
	"""
	Author: Akanksha Maurya
	Date: 10/05/2016
	"""

        def check_attempt(self, params):
                #unpack params
                self.attempt = params['attempt'] #student's attempt
                self.answer = params['answer'] #solution
                self.att_tree = params['att_tree'] #attempt tree
                self.ans_tree = params['ans_tree'] #solution tree

                hint=''


                try:

                        if  '^' in self.attempt and len(self.att_tree)==3 and self.att_tree[1][1]==2.0:
				hint="It seems you are counting both heads and tails output as event for each coin flip. "

                        if len(hint)>0:
                                return hint+'What is the number 2 heads in 4 coin flips?','C(4,2)'
                        else:
                                return '',''
                except Exception:
                        return '',''



	def get_problems(self):
		self.problem_list = ["Combinatorics/coinProblems/part3"]
		return self.problem_list
