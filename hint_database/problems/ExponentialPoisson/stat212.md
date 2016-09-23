```python
# random variables (no need to import random library)

ans1 = 0
mu = 0 
a = 0
x = 0
lambd = 0
while (0.002 > ans1) :
	mu = random.randrange(50,70,5) / 10
	lambd = 1 / mu
	a = random.randrange(9,12,1)
	x = lambd * a
	ans1 = math.exp(x)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "exp(-1/{0} * {1})".format(mu,a)

# Group all solutions into a list
solutions = [solution1]

```

The manager of a supermarket tracked the amount of time needed
for customers to be served by the cashier.  After checking with
his statistics professor, he concluded that the checkout times
are exponentially distributed with a mean of $mu minutes.  What
propotion of customers require more than $a minutes to check out?


* Proportion =

[_]
