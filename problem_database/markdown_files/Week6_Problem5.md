```python
# random variables (no need to import random library)

k = random.randrange(1,2,1);
r = random.randrange(1,2,1);
a = random.randrange(800,1200,100);
select = random.randrange(8,15,1);
s = a/10;

j = random.randrange(1,3,1);

x = random.randrange(12,15,1);
y = random.randrange(5,6,1);


# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "{0}*1/{1}".format(s,a)
solution2 = "C({0},{1})* ( (1/{2})^{1}) * ( (1-1/{2})^{{({0}-{1})}} )".format(s,j,a)
solution3 = "exp(-.1)*(.1)^{0}/{0}!".format(j)

# Group all solutions into a list
solutions = [solution1,solution2,solution3]

```

There is a typesetter who, on average, makes one mistake per $a words. Assume that he is setting a book with $s words to a page.  Let \\\(S_{$s}\\\) be the number of mistakes that he makes on a single page.

* What is the expected value of \\\(S_{$s}\\\)?

[_]

* What is the exact probability that \\\(S_{$s}\\\) = $j?

[_]

* What is the Poisson approximation of \\\(S_{$s}\\\) = $j?

[_]
