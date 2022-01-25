# imports/setup
from statistics import stdev
import numpy as np
#1. How many negative numbers are there?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print('There are', len(a[a < 0]), 'negative numbers.\n')

#2. How many positive numbers are there?
print('There are', len(a[a > 0]), 'positive numbers not including zero.\n')

#3. How many even positive numbers are there?
evn_num = a[a % 2 == 0] 
pos_evn = evn_num[evn_num > 0]
print(pos_evn)
print('There are',  len(pos_evn), 'numbers that are even and positive.\n')

#4. If you were to add 3 to each data point, how many positive numbers would there be?
a_plus_3 = a + 3
pos_num = a_plus_3[a_plus_3 > 0]
print(pos_num)
print('There are', len(pos_num), 'positive numbers not including zero.\n')

#5. If you squared the each number, what would the new mean and standard deviation be?
a_sq = a ** 2
a_sq_mean = round(sum(a_sq / len(a_sq)))
print(a_sq_mean)
a_sq_std = round(np.std(a_sq))
print(a_sq_std)
print(f'The rounded average would be {a_sq_mean} and the standard deviation is {a_sq_std}.\n')

#6. 


