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





Suppose you have been dealt 4\\\(\\heartsuit\\\) and 5 \\\(\\heartsuit\\\). What is the conditional probability that you will get a straight (five cards in sequence, but not all from the same suit) given that you have been dealt these two cards, and that the flop is "2\\\(\\clubsuit\\\), Q\\\(\\clubsuit\\\), K\\\(\\diamondsuit\\\)"

Consider following events,

Event A: You will get a straight.

Event B:  You have been dealt with 5 cards i.e. 4\\\(\\heartsuit\\\), 5 \\\(\\heartsuit\\\), 2\\\(\\clubsuit\\\), Q\\\(\\clubsuit\\\), K\\\(\\diamondsuit\\\).

In this case you need a 3 and either a 6 or A on the turn and river in order to get straight.

- The number of such card pairs, ignoring order, is the size of  \(|A \cap B| = \)  

[_]

The conditional probability:

\[P(A|B) = \frac{P(A \cap B)}{P(B)} =  \frac{|A \cap B|}{|B|} \]

- The conditional probability \(P(A|B) = \) 

[_]

