```python
n = random.randrange(10,20,1)

solution1 = "10!"
solution2 = "{0}!/({0}-3)!".format(n)

solutions = [solution1, solution2]
```

Suppose there are four children---Alice, Bill, Christie, and Doug---at an animal shelter, checking out the current pool of \\\(n\\\) dogs. Each child writes down the name of the dog he or she likes most. How many possible outcomes are there?

We can represent each outcome as a 4-tuple (Alice's choice, Bill's choice, Christie's choice, Doug's choice) in which each entry is the name of a dog. So the number of outcomes is \\\[n^4\\\]

Now suppose that these same children are actually picking out dogs. First Alice chooses a dog to adopt, then Bill chooses a dog to adopt, and so on. How many outcomes are there now?

In this situation, Alice has \\\(n\\\) choices, but Bill has only \\\(n-1\\\) choices, Christie has \\\(n-2\\\) choices, and Doug has \\\(n-3\\\) choices. So there are \\\(n(n-1)(n-2)(n-3)\\\) possible outcomes.

The first situation is called *sampling with replacement*: the outcomes are tuples in which the same element (dog) can occur more than once. The number of such \\\(k\\\) tuples, chosen from \\\(n\\\) elements, is \\\(n^k\\\)  In the example, \\\(k=4\\\)

The second situation is *sampling without replacement*: the outcomes are tuples in which no element can be repeated. The number of such \\\(k\\\) tuples, chosen from \\\(n\\\) elements, is

\\\[n(n-1)(n-2) \cdots (n-k+1)\\\]

Here's a related question: how many ways are there to order (shuffle) a deck of 52 cards?  (Each such ordering is called a *permutation* of the cards.) Well, the result is a 52-tuple, drawn from a set of size 52, in which no card is repeated. Therefore, the number of permutations is \\\(52 \cdot 51 \cdot 50 \cdots 1\\\)  which is called \\\(52 \\\)  *factorial* and denoted as \\\(52!\\\)  More generally, the number of permutations of \\\(n\\\) elements is \\\(n\\\) factorial or \\\(n!\\\)

To recap, how many ways are there to order 10 elements?

[_]

(you can use expressions such as 3*2 and 7! in your answer).

Coming back to sampling \\\(k\\\) out of \\\(n\\\) elements without replacement, we can write it succinctly as

\\\[ n(n-1)(n-2) \cdots (n-k+1) = \frac{n!}{(n-k)!} \\\]

*Question:*
Suppose you have a deck with $n different cards. How many ways are there to choose 3 cards out of this deck? (the order of the 3 picked out cards _does_ matter)

[_]
