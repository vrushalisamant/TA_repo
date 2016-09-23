```python
ns = random.randrange(4,6,1)
nr = random.randrange(10,16,1)
n = ns*nr;

solution1 = "C({0},5)".format(n)

solutions = [solution1]
```

## Probability of Poker Hands ##
You are given a deck of cards with *$ns suites* and *$nr ranks*. A hand consists of 5 cards from this deck, and may fall into one of the categories. We are going to compute the probability of each category.

The number of all possible hands is 

[_]
