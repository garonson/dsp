[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

### Answer to Exercise 2.4

# Q 2.4: Using the variable totalwgt_lb, investigate whether first ba- 
# bies are lighter or heavier than others. Compute Cohen’s d to 
# quantify the difference between the groups. How does it compare 
# to the difference in pregnancy length?"

import math
import os
import thinkstats2
os.chdir("/Users/Glen/ds/metis/metisgh/prework/ThinkStats2/code")
import nsfg
def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg(df)
    return df
df = nsfg.ReadFemPreg()
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
hist = thinkstats2.Hist(live.birthwgt_lb, label='birthwgt_lb')
#thinkplot.Hist(hist)
#thinkplot.Show(xlabel='pounds', ylabel='frequency')


firsts = live[live.birthord == 1].totalwgt_lb
others = live[live.birthord != 1].totalwgt_lb

firsts_lngth=live[live.birthord == 1].prglngth
others_lngth=live[live.birthord != 1].prglngth

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print("Cohen's D for birth weight by first vs later births ", CohenEffectSize(firsts, others))
print("Cohen's D for pregnancy length by first vs later births ", CohenEffectSize(firsts_lngth, others_lngth))

print("\nThe mean of 'other' births are 0.09 standard deviations higher than the typical pregnancy weight\n"
"The mean of 'other' births are on average 0.03 standard deviations lower than the typical pregnancy duration")
