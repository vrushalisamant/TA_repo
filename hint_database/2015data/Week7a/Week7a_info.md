##Week7a

### Sorted with number of attempts

problem 9 (Answer include variables): 2497

		 part  1 :  400
		 part  2 :  419
		 part  3 :  370
		 part  4 :  404
		 part  5 :  904


[problem 6](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_6_clusters.md): 1214

		 part  1 :  158
		 part  2 :  639
		 part  3 :  377
		 part  4 :  11
		 part  5 :  9
		 part  6 :  7
		 part  7 :  8
		 part  8 :  5


[problem 2](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_2_clusters.md): 945

		 part  1 :  511
		 part  2 :  324
		 part  3 :  48
		 part  4 :  62


[problem 7](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_7_clusters.md): 559

		 part  1 :  159
		 part  2 :  181
		 part  3 :  82
		 part  4 :  66
		 part  5 :  71


[problem 8](https://github.com/cse103/Attempt_Analysis/blob/master/clustering_code/clusters/Week7a/md_files/Week7a_8_clusters.md): 204

		 part  1 :  84
		 part  2 :  120


problem 1 (Multiple Choice): 49

		 part  1 :  49


### Problem Content

Problem 1:

	Multiple choice problem



Problem 2:

      $a = Compute("0.05/sqrt(0.16/200)");
      $q = Compute("Q($a)");

      A noted psychic was tested for extrasensory perception. The psychic was presented
      with 200 cards face down and asked to determine if the card were one of five symbols.
      The psychic was correct in 50 cases. Let p represent the probability that the psychic
      correctly identifies the symbol on the card in a random trial. Assume the 200 trials
      can be treated as a simple random sample.

      Suppose you wished to see if there were evidence that the psychic is
      doing better than just guessing. To do this, you test the hypotheses [`H_0 : p = .20`]
      versus [`H_{alternative} : p > .20`].

      What is the z-score? [__________________________________________]{$a}

      What is the p-value for the test statistic? (You can use Q function in the answer) [_________]{$q}

      Can you reject at the .05 significance level? (answer "yes" or "no") [_______]{"yes"}

      Can you reject at the .01 significance level? (answer "yes" or "no") [_______]{"no"}


Problem 3:

	Multiple choice problem


Problem 4:

	Multiple choice problem


Problem 5:

	Missing from database :(




Problem 6:

      Suppose there are 3 species of fish in the world, we are interested
      in two fish populations: fish of the pacific ocean and fish of the atlantic ocean.
      Each one of these populations is characterized by a distribution over the species of fish:
      The pacific distribution is uniform over the 3  species:
      [`P_p=(1/3,1/3,1/3)`] while in the atlantic population the first species is twice more common thand the other two: [`P_a=(1/2,1/4,1/4)`]

      Suppose we are given a  batch of 65 fish whose source is unknown.
      The number of fish of each species is [`(30,20,15)`].

      We would like to know whether the the batch of fish is from the atlantic or the pacific (or both).

      One way of formalizing this problem is to consider two Null hypotheses:

      * HA = the batch is from the atlantic ocean. More technically, the batch was sampled from the distribution [`P_a`]
      * HP = the batch is from the pacific ocean. More technically, the batch was sampled from the distribution [`P_b`].

      The test that we will use is the [`\chi^2`] test. (https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test).

      The [`\chi^2`] test statistic is

      [``\chi^2 =  N \sum_{i=1}^n p_i \left(\frac{O_i/N - p_i}{p_i}\right)^2``]

      Where:
      * [`n`] is the number of species (3 in our case).
      * [`p_i`] is the probability of the [`i`]'th species according to the Null distribution.
      * [`O_i`] is the number of observations of species [`i`]
      * [`N`] is the total number of observation. [`N=\sum_{i=1}^n O_i`]. Which is [_____]{65} in our case.

      Write expressions for the [`\chi^2`] statistic for the two null Hypotheses:

      * For hypothesis HA ( batch is from atlantic ocean), [`\chi^2=`] [___________________________________________________________________]{Compute("65*(0.500*(((30.0/65.0)-0.500)/0.500)**2+0.250*(((20.0/65.0)-0.250)/0.250)**2+0.250*(((15.0/65.0)-0.250)/0.250)**2)")}
      * For hypothesis HP ( batch is from pacific ocean), [`\chi^2=`] [___________________________________________________________________]{Compute("65*((1./3)*(((30.0/65.0)-(1./3))/(1./3))**2+(1./3)*(((20.0/65.0)-(1./3))/(1./3))**2+(1./3)*(((15.0/65.0)-(1./3))/(1./3))**2)")}

      This question continues with the next problem.




Problem 7:

      To compute the p-value of rejecting the Null hypothesis we need to know the **number of degrees of freedom** of the distribution. As the size of the space is 3 there are three variables defining the distribution: [`p_1,p_2,p_3`] as these probabilities sum to one there [`v=2`] degrees of freedom. We then use the CDF for the [`\chi^2`] distribution with 2 degrees of freedom to calculate the p-values.

      Answer the following questions yes (enter +1) or no (enter -1)

      * A small value of the [`\chi^2`] statistic justifies **rejecting** the Null Hypothesis [______]{-1}
      * A small value of the [`\chi^2`] statistic justifies **accepting** the Null Hypothesis [______]{-1}
      * A large value of the [`\chi^2`] statistic justifies **rejecting** the Null Hypothesis [______]{+1}
      * It is possible to reject both of the Null hypotheses:[__________]{+1}
      * It is possible to not reject either of the Null hypotheses: [___________]{+1}




Problem 8:

      Using the data given in the problem regarding the source of a batch of fish we get the following:
      * The p-value associated with rejecting the HA hypothesis is 0.5616
      * The p value associated with rejecting the HP hypothesis is  0.0677

      Which hypothesis can we reject if we set our confidence level to be [`\alpha=10%`] ?
      (use 1 for reject, 0 for not reject)

      * We can reject the hypothesis that the batch is from the pacific ocean [____]{1}
      * We can reject the hypothesis that the batch is from the atlantic ocean [_____]{0}




Problem 9:

      ## Counting the number of fish in a lake.
      A lake contains an unknown number of fish. 1000 of them are caught, marked with red spots, and then
      returned to the water. Later, a random subset of 100 fish are caught from the lake, and it is found
      that [`x`] of them have red spots.
      1. In terms of [`x`], what estimate would you give for the number of fish in the lake?  [_______]{"1000*100/x"}
      2. Let n be the true number of fish in the lake. Then distribution of the random variable X (the number of fish in your second sample of size 100), follows a Binomial distribution with what parameters?  [`\mathbb{E}(X) = `][______]{"100*1000/n"} and [`\mbox{var}(X) = `][______]{"100*(1000/n)*(1-1000/n)"}  Give your answers in terms of [`n`].
      3. For standard normal random variable [`S`], what is [`P(-1.96 < S < 1.96)`]?  [_________]{"1-2*0.025"}
      4. If you had to give a 95% confidence interval of [`\mathbb{E}(X)`] in terms of [`n`], what would it be?  [`X\pm`][_______]{"1.96*sqrt(100*(1000/n)*(1-1000/n))"}
      5. Use the approximation technique you learned from class, the confidence interval of [`n`] is from [____________]{"1000*100/(x + sqrt(100))"} to [____________]{"1000*100/(x - sqrt(100))"}
