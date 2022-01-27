# imports/setup
from statistics import mean, stdev
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
a_sq = a[a ** 2]
a_sq_mean = round(sum(a_sq / len(a_sq)))
print(a_sq_mean)
a_sq_std = round(np.std(a_sq))
print(a_sq_std)
print(f'The rounded average would be {a_sq_mean} and the standard deviation is {a_sq_std}.\n')

#6. A common statistical operation on a dataset is centering.
# This means to adjust the data such that the mean of the data is 0.
# This is done by subtracting the mean from each data point.
# Center the data set.
print(a)
a_mean = np.mean(a)
print(f'The mean of a is {a_mean}.\n')
a_cent = a - int(a_mean)
print('Centered data:') 
print(a_cent)

#7. Calculate the z-score for each data point. 
a_std = np.std(a)
z_score = (a - a_mean) / a_std
print('The z scores are:')
print(z_score)

#-------------------------------------------------------------------

#8. MORE NUMPY PRACTICE 
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = np.sum(a)
print(f'The sum of a is {sum_of_a}.\n')
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(f' The min of a is {min_of_a}.\n')
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(f'The max number in a is {max_of_a}.\n')
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = np.mean(a)
print(f'The mean of a is {mean_of_a}.\n')
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.product(a)
print(f'The product of a is {product_of_a}.\n')
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = np.square(a)
print('The squares of a are as follows:')
print(squares_of_a)
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
a = np.array(a)
odds_in_a = a[a % 2 == 1] 
print('Odd numbers are as follow:')
print(odds_in_a)
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0] 
print(' numbers are as follow:')
print(evens_in_a)
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)

sum_of_b = 0
for row in b:
    for n in row:
        sum_of_b += sum(row)
print(sum_of_b)
#ans
sum_of_b = b.sum()
print('The sum of b the numpy way is:')
print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
#ans
min_of_b = b.min()
print(min_of_b)
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
#ans
max_of_b = b.max()
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
#ans
mean_of_b = b.mean()
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
#ans
product_of_b = b.prod()
print(product_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
#ans
squares_of_b = b**2
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
#ans 
odds_in_b = b[b % 2 == 1]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
#ans
evens_in_b = b[b % 2 == 0]
print(evens_in_b)
# Exercise 9 - print out the shape of the array b.
print(b.shape)

# Exercise 10 - transpose the array b.
b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.flatten()

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(1, 6)
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c.prod()
# Exercise 2 - Determine the standard deviation of c.
c.std()
# Exercise 3 - Determine the variance of c.
c.var()
# Exercise 4 - Print out the shape of the array c
c.shape
# Exercise 5 - Transpose c and print out transposed result.
c.T
# Exercise 6 - Get the dot product of the array c with c. 
c.dot(c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c * c.T
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(c*c.T).prod


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
# Exercise 4 - Find all the negative numbers in d
d[d < 0]
# Exercise 5 - Find all the positive numbers in d
d[d > 0]
# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
np.unique.size
# Exercise 8 - Print out the shape of d.
print(d.shape)
# Exercise 9 - Transpose and then print out the shape of d.
d_sh = d.shape
d_sh_T = d_sh.T
print(d_sh)
# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)