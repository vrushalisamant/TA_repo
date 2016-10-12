# Make sure you name your file with className.py
# To test your class make sure you add the local path of hint_class_helpers in your system path
from hint_class_helpers.find_matches import find_matches
class Prob3_Part1:
	"""
	Author: Vrushali Samant
	Date: <10-11-2016 14:00>
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree
                matches = find_matches(params)       
                #print "Prob3_Part1 matches: ", matches

                for m in matches:
                        if 'R.0' not in m:
                                return "If you have n digits and m choices per digit, what should be the base for your exponential expression?","{0}".format("m")
                        if 'R.1' not in m:
                            return "If you have n digits and m choices per digit, what should be the exponent in your expression?", "{0}".format("n")

                if ("^" not in self.attempt):
                    return "If there are n digits and m choices for each digit, what format should your answer be in?", "{0}^{1}".format("a","b")
                else:
                    return "If there are n spots, and m choices for each spot, is the total number of combinations n^m or m^n?","{0}^{1}".format("m","n") 
                return "", ""

	def get_problems(self):
		self.problem_list = ["Combinatorics/DiscreteProb1/part1"]
		return self.problem_list
