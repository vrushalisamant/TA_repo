# Make sure you name your file with className.py

from sets import Set

from Parse_tree_properties import collect_terms

class Prob13_Part1:
	"""
	Author: Yoav Freund
	Date: 9/25/2016
	"""

	def check_attempt(self, params):
                #unpack params
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

                # all print commands inside a check_attempt filter are for debugging only and should be disabled before deploying the hint.
                print 'Prob13_Part1',self.answer,self.attempt #debug print

                #check if the form of the parse tree has the right
                #shape: an operator and two leafs that correspond to
                #the operands
                if len(self.att_tree)==3 and self.att_tree[1][0]=='X' and self.att_tree[2][0]=='X':
                        print 'attempt_tree=\n',self.att_tree #debug

                        # Preparations ---------------------------------------
                        parts={}  # A dictionary of dictionaries that
                                  # holds the 3 parts of the attempt
                                  # and the three parts of the answer.
                        operands={} # A dict of Sets which holds the
                                    # operands in the attempt and the
                                    # operands in the answer.
                        for tree_name,tree in [('att',self.att_tree),('ans',self.ans_tree)]:
                                parts[tree_name]={'op':tree[0][0],
                                                  'a':tree[1][1],
                                                  'b':tree[2][1]}
                                operands[tree_name]=Set([tree[1][1], tree[2][1]])
                                print 'using collect term on',tree_name,collect_terms(tree)
                        print 'parts=', parts  
                        print 'operands',operands

                        # identifying mistakes
                        if parts['att']['b']==2:
                                return 'It seems that you have the order of the operands reversed, What is the number of binary strings of length 3? [_]','2^3'
                        
                        # unrecognized = the set of terms (numbers)
                        # that appear in the attempt but not in the
                        # answer.
                        unrecognized=operands['att']-operands['ans']

                        print 'unrecognized=',unrecognized
                        if len(unrecognized)>0:
                                hint='The numbers in the question are '+','.join([str(x) for x in operands['ans']])
                                hint+='. Where did '+','.join([str(x) for x in unrecognized])+\
                                        ' come from? \n Please replace with expression using the number in the question'
                                return hint,''
                        
		return 'Prob13_part1'+str(self.att_tree),""

	def get_problems(self):
		self.problem_list = [("Combinatorics/p13",1)]
		return self.problem_list
