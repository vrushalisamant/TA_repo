```python
import math

def combination(n,k):
    return math.factorial(n)/(math.factorial(n - k) * math.factorial(k))

nCards=random.randrange(4,7,1)
b=random.randrange(2,nCards-1,1)

solution1 = "C(52,{0})".format(nCards)
solution2 = "4"
solution3 = "C(13,{0})".format(b)
solution4 = "52 - 13"
solution5 = "C(39, {1} - {0})".format(b,nCards)
solution6 = "4*C(13,{0})*C(39,{1}-{0})".format(b,nCards)
solution7 = "4*C(13,{0})*C(39,{1}-{0})/C(52,{1})".format(b,nCards)

solutions = [solution1,solution2,solution3,solution4,solution5,solution6, solution7]
```
## Probability of cards of the same suite ##
A poker hand consisting of $nCards cards is dealt from a standard deck of 52 cards.
Find the probability that the hand contains exactly $b cards of the same suite. It is allowed to have any number of cards in other suites.

First, we know the number of all possible hands of $nCards cards is 

[_]

Then, we calculate the number of hands that contain exactly $b cards of the same suite.

We first choose which suite the $b cards is. Obviously, there are 

[_]

possibilities.

The number of possibilities for the ranks of these cards is 

[_]

The other $nCards-$b cards in the hand can be any cards that has a different suite than the $b cards. There are a total of 

[_]

such cards. To choose $nCards-$b from them, there are 

[_]

possibilities.

Thus we can compute the number of hands that have exactly $b cards of the same suite, which is 

[_]

Finally we can calculate the probability of such hands, by calculating th ratio of the number of such hands to the number of all hands. This is 

[_]
