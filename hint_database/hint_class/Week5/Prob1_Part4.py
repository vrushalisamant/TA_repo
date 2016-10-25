class Prob1_Part4:
    """
    Author: LIU HAN
    Date: 10/24/2016
    """

    def check_attempt(self, params):
        # unpack params
        self.attempt = params['attempt']  # student's attempt
        self.answer = params['answer']  # solution
        self.att_tree = params['att_tree']  # attempt tree
        self.ans_tree = params['ans_tree']  # solution tree

        hint = ''

        try:
            hint = 'The component weights of two distribution should be summed to 1.' \
                   'For example:F = 0.4X + 0.6*Y where X and Y are two random variable with certain ' \
                   'distribution. Then, the weight component for X is 0.4 and 0.6 for Y.'

            if len(hint) > 0:
                return hint
            else:
                return '', ''
        except Exception:
            return '', ''

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_uni/part4"]
        return self.problem_list