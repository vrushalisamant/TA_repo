```python
ns = random.randrange(4,6,1);
nr = random.randrange(10,16,1);
n = ns*nr;

solution1 = "{0}-3".format(nr)
solution2 = "{0}^5 - {0}".format(ns)
solution3 = "({1}-3)*({0}^5-{0})".format(ns,nr)
solution4 = "({1}-3)*({0}^5-{0})/C({2},5)".format(ns,nr,n)

solutions = [solution1,solution2,solution3,solution4]
```

### Straight : Five cards in sequence, but not all from the same suit ###
*Remember, the deck you are using has $ns suits and $nr ranks.*

* In the case of a standard deck, the ranks of a straight is one of (Ace,2,3,4,5) ... (10,J,Q,K,Ace). Similarly, in your deck, the number of possibilities for the ranks of a straight is 

[_]

* The suits can be anything other than all equal, so the number of possibilities for the suits of a straight is

[_]

* Thus the number of hands that is a straight is 

[_]

* The ratio of this number to the number of all hands 

[_]