def check_attempt(p):
	if p['att_tree'][0] == 'X' and p['ans_tree'][0] != 'X':
		return "Your answer is incorrect, please write an expression."
	return ""