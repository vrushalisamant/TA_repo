```python
# random variables (no need to import random library)
a = random.randrange(10,50,1) / 10
b = random.randrange(10,50,1) / 10

while (0.5 > abs(a - b)):
	b = random.randrange(10,50,1) / 10



# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "(exp(-{0}) + exp(-{1}))/2".format(a,b)


# Group all solutions into a list
solutions = [solution1]

```

A certain typing agency employs two typists. The average number of errors per article is
 $a when typed by the first typist and $b when typed by the second.


* If your article is equally likely to be typed by either typist, find the probability
that it will have no errors.

[_]
