class Prob3_Part5:
    """
    Author: Liu Han
    Date: 10/31/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = ''

        try:
            if not '+' in self.attempt:
                hint = 'Should P(Y=2) equal to the sum of probabilities of all cases when Y = 2?'

            if len(hint) > 0:
                return hint + 'Suppose P(Y = 2|X = 1) = 1/3, and P(Y = 2|X = 2) = 1/3 (Note: The value ' \
                              'of X can only be 1 or 2); What is P(Y = 2)?', '2/3'
            else:
                return '', ''

        except Exception:

            return '', ''

    def get_problems(self):
        self.problem_list = ["Covariance/ContingencyTables5/part5"]
        return self.problem_list