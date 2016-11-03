```python
# variable names and values
# if multiple variables, the number of values to test should be the same
variable_values = {'x':[20,50,80], 'n':[5000,2000,1250]}

# value index used to extract hint
index_of_test_value = 2

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
solution1 = "1000*100/x"
solution2 = "100*1000/n"
solution3 = "100*(1000/n)*(1-1000/n)"
solution4 = "1-2*0.025"
solution5 = "1.96*sqrt(100*(1000/n)*(1-1000/n))"
solution6 = "1000*100/(x + sqrt(100))"
solution7 = "1000*100/(x - sqrt(100))"


# Group all solutions into a list
solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7]

```

## Counting the number of fish in a lake.
A lake contains an unknown number of fish. 1000 of them are caught, marked with red spots, and then
returned to the water. Later, a random subset of 100 fish are caught from the lake, and it is found
that \\\(x\\\) of them have red spots.

*1. In terms of \\\(x\\\), what estimate would you give for the number of fish in the lake?

[_]

*2. Let n be the true number of fish in the lake. Then distribution of the random variable X (the number of fish in your second sample of size 100), follows a Binomial distribution with what parameters?

\\\(\mathbb{E}(X) = \\\)

[_]

\\\(\mbox{var}(X) = \\\)

[_]

*3. For standard normal random variable \\\(S\\\), what is \\\(P(-1.96 < S < 1.96)\\\)?

[_]

*4. If you had to give a 95% confidence interval of \\\(\mathbb{E}(X)\\\) in terms of \\\(n\\\), what would it be?  

\\\(X\pm = \\\)

[_]

*5. Use the approximation technique you learned from class, the confidence interval of \\\(n\\\) is

from

[_]

to

[_]
