import pandas as pd
import numpy as np
from scipy import stats

linux_approach = np.array([3692, 3692,3652])
pandas_approach = np.array([5680116, 5680240, 5680412])

mean1 = linux_approach.mean()
stdev1 = linux_approach.std()
mean2 = pandas_approach.mean()
stdev2 = pandas_approach.std()
print("Linux Approach ->", "Mean:", mean1, "and", "Standard deviation:", stdev1)
print("Pandas Approach ->", "Mean:", mean2, "and", "Standard deviation:", stdev2)


statistic, p = stats.ttest_ind(linux_approach, pandas_approach)
print("p-value: ", p)
print('''A p-value of 0.00 indicates that the null can be rejected. 
There is a statistically significant difference between the mean maximum memory of the linux approach and pandas approach.''')