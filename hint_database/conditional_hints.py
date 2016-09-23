import cluster_functions
from search import search

def conditional_hint(id_str, p):
    return search(id_str, p)

def conditional_hint_w_variables(p, variables):
    """
    input variables should be a list of strings of variable names 
    """
    return "", ""
