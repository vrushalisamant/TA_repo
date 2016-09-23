```python
ns = random.randrange(4,6,1)
nr = random.randrange(10,16,1)
n = ns*nr

solution1 = "{0}".format(nr)
solution2 = "{0}-1".format(nr)
solution3 = "C({0},3)".format(ns)
solution4 = "C({0},2)".format(ns)
solution5 = "{0}*({0}-1)*C({1},3)*C({1},2)".format(ns,nr)
solution6 = "{1}*({1}-1)*C({0},3)*C({0},2)/C({2},5)".format(ns,nr,n)

solutions = [solution1,solution2,solution3,solution4,solution5,solution6]  
```

### Full House: 2 of one rank and 3 of another rank ###
*Remember, the deck you are using has $ns suits and $nr ranks.*

* The number of possibilities for the rank of the triple is 

[_]

* Given the rank of the triple, the number of possibilities for the rank of the pair is 

[_]

* The number of possibilities for the suit of the triple is 

[_]

* The number of possibilities for the suit of the pair is 

[_]

* Thus the number of hands that is a full house is 

[_]

* The ratio of this number to the number of all hands 

[_]