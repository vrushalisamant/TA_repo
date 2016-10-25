class Prob1_Part3:
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
            hint = 'For uniform component interval, look at the image to find where the graph is not ' \
                   'curved and that is where the interval is.'

            if len(hint) > 0:
                return hint
            else:
                return '', ''
        except Exception:
            return '', ''

    def get_problems(self):
        self.problem_list = ["CumulativeDistributionFunctions/cdf_exp_uni/part3"]
        return self.problem_list