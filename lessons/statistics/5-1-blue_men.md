[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

from __future__ import print_function, division

%matplotlib inline
import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

# distribution parameters
mu = 178                                        # median of 178cm height (avg US Male)
sigma = 7.7                                     # 7.7cm height mean (avg US male)
dist = scipy.stats.norm(loc=mu, scale=sigma)    # normal distribution based on above

# check CDF of distribution; ~16% are one standard deviation below mean
dist.cdf(mu-sigma)

# answer to question 'How many people are between 5'10" and 6'1"?'
low = dist.cdf(177.8)                           # = to 5'10"
high = dist.cdf(185.4)                          # = to 6'1"
low, high, high-low

print("A candidate who is 5\'10\" is taller than 49% of the US male population,\n"
"A candidate who is 6\'1\" is taller than 83% of the US male population,\n"
"34% of the US male population meets the height requirement for the Blue Man Group")
