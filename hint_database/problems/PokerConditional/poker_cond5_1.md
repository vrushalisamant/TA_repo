```python
import math
# random variables (no need to import random library)

def cnk(n, k):
    return math.factorial(n)/(math.factorial(n - k) * math.factorial(k)) 

a1 = cnk(32, 5) - cnk(20, 5)
a2 = cnk(52, 5) - cnk(40, 5)
a3 = (cnk(32, 5)-cnk(20, 5))/(cnk(52, 5)-cnk(40, 5))

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "{0}".format(a1)
solution2 = "{0}".format(a2)
solution3 = "{0}".format(a3)


# Group all solutions into a list
solutions = [solution1, solution2, solution3]


```





* Find the probability that a poker hand of 5 cards from a standard deck will contain no card smaller than 7 (i.e. 2,3...6) (call this event \\\(A\\\)), given that it contains at least one face card (i.e. J, Q, K) (call this event \\\(B\\\))
We define two events:

* Event \\\(A\\\): The hand contains no card smaller than 7.

* Event \\\(B\\\): The hand contains at least one face card.

We first compute the size of the relevant events \\\(|A \\cap B| = \\\)

[_]

\\\(|B| = \\\)

[_]

We then use the ratio between the sizes of the events to find the conditional probability:

- The conditional probability \\\(P(A|B) = \\\)

[_]

