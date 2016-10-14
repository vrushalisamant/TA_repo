```python
import math
# random variables (no need to import random library)

def cnk(n, k):
    return math.factorial(n)/(math.factorial(n - k) * math.factorial(k))

a1 = 1-3/cnk(52-7,2)
a2 = (1-3/cnk(52-7,2))*(1-3/cnk(52-9,2))

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "3"
solution2 = "{0}".format(a1)
solution3 = "{0}".format(a2)


# Group all solutions into a list
solutions = [solution1, solution2, solution3]


```



Like the previous question, suppose you have been dealt "4\\\(\\heartsuit\\\), 5\\\(\\heartsuit\\\)".

1. Suppose you have one opponent. What is the conditional probability that you will win, given these two cards in hand, and that the board is "3\\\(\\diamondsuit\\\), 4\\\(\\diamondsuit\\\), 4\\\(\\clubsuit\\\), 4\\\(\\spadesuit\\\), 5\\\(\\diamondsuit\\\)"?
   
    - With this board, we have four of a kind. The only way the opponent will beat it is with a straight flush. How many possible two cards does the opponent have that can make a straight flush, regardless of order? 

...(Recall that a straight flush is five cards in sequence of the same suit. This means that Given that there are three sequential diamonds on the table, think about which/how many pairs of diamonds could complete the 3,4,and 5 of diamonds to create such a sequence).  
    
    [_]
    
    - The conditional probability that you will win is the complement of the probability that they will, out of all the remaining cards, have in their hand the necessary cards for a straight flush:
     
    [_]

2. What if you have two opponents? What is the conditional probability that you will win?

...(Take into account that opponent A and opponent B could have the straight flush.)
    
    - The conditional probability that you will win is 
    
    [_]
