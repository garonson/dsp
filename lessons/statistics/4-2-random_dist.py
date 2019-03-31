[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

from __future__ import print_function, division

%matplotlib inline
import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

# generate PMF with 1000 values between 0, 1
t = np.random.random(1000)
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Config(xlabel='Random variate', ylabel='PMF')

# generate CDF with 1000 values between 0, 1
cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random variate', ylabel='CDF')

# print answer to question
print("The data in the CDF are distributed uniformly.\n"
"These same data do not display well in the PMF because there\n",
"are 1000 values in the dataset and their distribution is uniform.\n"
"Thus in this case the CDF is the superior visualization.")
