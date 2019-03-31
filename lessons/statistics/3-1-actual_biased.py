[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# Use the NSFG respondent variable NUMKDHH to construct the actual distribu- 
# tion for the number of children under 18 in the household. Now compute the 
# biased distribution we would see if we surveyed the children and asked them 
# how many children under 18 (including themselves) are in their household.
# Plot the actual and biased distributions, and compute their means. 

from __future__ import print_function, division

%matplotlib inline
import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biased = BiasPmf(pmf, label='biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

print("Solution to 3.1\n")
print("PMF mean: ", pmf.Mean())
print("Biased PMF mean: ", biased.Mean())

# PMF mean = 1.024205155043831 -- this is the actual distribution for the 
# number of children under 18 in the household

# Biased PMF mean = 2.403679100664282 -- this is the biased distribution for
# the number of children under 18 in the household. It is similar to the 
# class size paradox because families with more children will be overrepresented
# due to the sampling methodology, and families without children won't be represented
# at all

