```python
# random variables (no need to import random library)
#false burglary percentage
atpt = random.randrange(92,96,1)
perc = atpt/100

#burglary percentage
fals = random.randrange(1,3,1)
fperc = fals/100
sol = (perc/10000)/(perc*0.0001+ fperc*0.9999)

# Solutions with variables converted to string
# Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
solution1 = "1/10000"
solution2 = "{0}*0.0001 + {1}*0.9999".format(perc, fperc)
solution3 = "{0}*0.0001*100".format(perc)
solution4 = "{0}".format(sol)

# Group all solutions into a list
solutions = [solution1, solution2, solution3, solution4]


```

## Bayes' Burglary ##
o  The following example is taken from _Probabilistic Reasoning in Intelligent Systems_ by Judea Pearl:

You wake up in the middle of the night to the shrill sound of your burglar alarm. What is the chance that a burglary attempt has taken place? The relevant facts are: 

o  There is a $atpt% chance that an attempted burglary attempt will trigger the alarm. That is 
\\\[P(\\mbox{alarm} | \\mbox{burglary}) = $perc\\\]

o  There is a $fals% chance of a false alarm.
\\\[P(\mbox{alarm} | \mbox{no burglary}) = $fperc\\\]

o  Based on local crime statistics, there is a one-in-10,000 chance that a house will be burglarized on a given night.
.  what is \\\(P(\mbox{burglary})\\\)

[_]

o  We are interested in the chance of a burglary given that the alarm has sounded. We can use the conditional probability formula for this:
\\\[P(\\mbox{burglary} | \\mbox{alarm}) \\ = \\ \\frac{P(\\mbox{burglary, alarm})}{P(\\mbox{alarm})} \\ = \\ \\frac{P(\\mbox{alarm} | \\mbox{burglary}) P(\\mbox{burglary})}{P(\\mbox{alarm})}\\\]

o  The one term we don't immediately know is \\\(P(\mbox{alarm})\\\).  By the summation rule,
\\\[P(\\mbox{alarm}) \\ = \\ P(\\mbox{alarm} | \\mbox{burglary}) P(\\mbox{burglary}) + P(\\mbox{alarm} | \\mbox{no burglary}) P(\\mbox{no burglary})\\\]

.  What is \\\(P(\\mbox{alarm})\\\)?

[_]

.  What is \\\(P(\\mbox{burglary}, \\mbox{alarm})*100\\\)

[_]

.  Putting it all together, using the conditional probability definition mentioned above, what is
\\\[P(\\mbox{burglary} | \\mbox{alarm})\\\]

[_]

Thus our belief in a burglary has risen approximately a hundredfold from its default value of \\\(10^{-4}\\\)  on account of the alarm.
It is frequently the case, as in this example, that we wish to update the chances of an event \\\(H\\\) based on new evidence \\\(E\\\)  In other words, we wish to know \\\(P(H | E)\\\)
o  The derivation above implicitly uses the following formula, called Bayes Rule:
\\\[P(H | E)\\ = \\ \\frac{P(E|H) P(H)}{P(E)}\\\]


---
