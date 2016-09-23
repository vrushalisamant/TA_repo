```python
# random variables (no need to import random library)
p_men = random.randrange(6,8,1)
p_women = random.randrange(3,5,1)
p_male_given_colorblind = p_men/(p_men+p_women)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "{0}/({0}+{1})".format(p_men, p_women)


# Group all solutions into a list
solutions = [solution1]


```


Suppose that there are equal numbers of men and women in the world, and that \\\($p_men\\\)% of men are colorblind \\\($p_women\\\)% of women are colorblind. A person is chosen at random and found to be colorblind. What is the probability that the person is male? 

[_]

Reverse the condition:
\\\[\\textbf{Pr}(\\text{male}|\\text{colorblind}) = \\frac{Pr(\\text{male}, \\text{colorblind)}}{\\textbf{Pr}(\\text{colorblin)}} = \\\]
\\\[\\frac{\\textbf{Pr}(\\text{colorblind}|\\text{male})\\textbf{Pr}(\\text{male})}{\\textbf{Pr}(\\text{colorblind})}\\\]

Law of total probability + Bayes rule:
\\\[\\textbf{Pr}(\\text{colorblind}) = \\text{Pr}(\\text{male}, \\text{colorblind}) + \\textbf{Pr}(\\text{female}, \\text{colorblind}) =\\\]
\\\[\\textbf{Pr}(\\text{colorblind}|\\text{male})\\textbf{Pr}(\\text{male}) + \\textbf{Pr}(\\text{colorblind}|\\text{female})\\textbf{Pr}(\\text{female})\\\]

___