```python
a = random.randrange(300,400,1)
b = random.randrange(15,25,1)

solution1 = "10!/(2!8!) * 0.5^{10}"
solution2 = "10!/(1!9!) * 0.5^{10}"
solution3 = "1 * 0.5^{10}"
solution4 = "10!/(2!8!) * 0.5^{10}+ 10!/(1!9!) * 0.5^{10} + 1 * 0.5^{10}"
solution5 = "1- ( 10!/(2!8!) * 0.5^{10}+ 10!/(1!9!) * 0.5^{10} + 1 * 0.5^{10})"
solution6 = " (1- ( 10!/(2!8!) * 0.5^{10}+ 10!/(1!9!) * 0.5^{10} + 1 * 0.5^{10}) ) ^ $a "
solution7 = " 1 -  ((1- ( 10!/(2!8!) * 0.5^{10}+ 10!/(1!9!) * 0.5^{10} + 1 * 0.5^{10}) ) ^ $a ) "

solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7]
```

There is a class of $a students taking a T/F quiz of 10 questions. We would normally think it unlikely that a student would get more than 2 questions right out of 10 by flipping a coin, but with a class this large, it might be possible. Here we'll calculate the probability of at least one student in the class of size [$a] getting more than 2 questions right.

* What is the probability of a particular student getting exactly 2 questions right? 

[_]

* What is the probability of a particular student getting exactly 1 question right?

[_]

* What is the probability of a particular student getting no questions right? 

[_]

* What is the probability of a particular student getting at most 2 questions right?

[_]

* What is the probability of a particular student getting 3 or more questions right?

[_]

* What is the probability of every student in the class getting 3 or more questions right?

[_]

* What is the probability of some student in the class getting at most 2 questions right?

[_]