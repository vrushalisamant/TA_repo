```python
import math
# random variables (no need to import random library)
def cnk(n, k):
    return math.factorial(n)/(math.factorial(n - k) * math.factorial(k))

a1 = (4 * 8) / cnk(52 - 5, 2)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "4*8"
solution2 = "{0}".format(a1)


# Group all solutions into a list
solutions = [solution1, solution2]


```





*Suppose you have been dealt 4\\\(\\heartsuit\\\) and 5 \\\(\\heartsuit\\\). What is the conditional probability that you will get a straight given that you have been dealt these two cards, and that the flop is "2\\\(\\clubsuit\\\), Q\\\(\\clubsuit\\\), K\\\(\\diamondsuit\\\)"

In this case we need a 3 and either a 6 or A on the turn and river.

- The number of such card pairs, ignoring order, is 

[_]

- The conditional probability is 

[_]

