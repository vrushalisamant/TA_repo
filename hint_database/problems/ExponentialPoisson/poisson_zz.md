```python
# random variables (no need to import random library)
x = random.randrange(8,10,1);
X = x*x;
y = random.randrange(1,5,1);
lambd = 400/(X);

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "400/{0}".format(X)
solution2 = "exp({{-400/{0}}})*(400/{0})^{{{1}}}/({1}!)".format(X,y)
solution3 = "({0}*{0})*(exp({{-400/{1}}})*(400/{1})^{{{2}}}/({2}!))".format(x,X,y)

# Group all solutions into a list
solutions = [solution1, solution2, solution3]

```

You will be using Poisson Distribution in this problem. Review: a discrete random variable \\\(X\\\) is said to have a Poisson distribution with parameter \\\(\lambda > 0\\\), if for k = 0, 1, 2, ... the probability mass function of \\\(X\\\) is given by:

\\\[\Pr(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}\\\]

Assume that you live in a district of size \\\($x\\\) blocks by \\\($x\\\) blocks so that the total district is divided into \\\($X\\\) small squares. How likely is it that the square in which you live will receive \\\($y\\\) hits if the total area is hit by \\\(400\\\) bombs. Assume the probability that a particular bomb will hit your square with probability \\\(1/$X\\\).

* What is \\\(\lambda\\\) in the Poisson Distribution?

[_]

* Using Poisson Distribution, what is the approximate probability that your square will receive \\\($y\\\) hits?

[_]

* What is the expected number of squares that will receive exactly \\\($y\\\) hits using the approximate probability from above?

[_]