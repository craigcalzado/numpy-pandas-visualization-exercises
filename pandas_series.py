#---------- EXERCISES PART I ---------- 
#setup
from distutils.command.clean import clean
from itertools import count
import numpy as np
import pandas as pd
import matplotlib as plt

array_fruits = np.array(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruits = pd.Series(array_fruits)
print(fruits)

#1. Determine the number of elements in fruits.
fruits.count()

#2. Output only the index from fruits.
fruits.index

#3. Output only values from fruits.
fruits.values

#4. Confirm the data type of the  values in fruits.
a = type(fruits[1])
b = type(fruits.values)
c = type(fruits)
print(F'The data types with fruits are as follows:\n {a}\n {b}\n {c}\n')

#5. Output only the first five values from fruits. Output the last three values.
# Output two random values from fruits.
fruits.head()
fruits.tail(3)
fruits.sample(2)

#6. Run the .describe() on fruits to see what information 
# it returns when called on a Series with string values.
fruits.describe()

#7. Run the code necessary to produce only the unique string values form fruits.
fruits.unique()

#8 Determine how many times each unique string value occurs in fruits.
fruits.value_counts()

#9. Determine the string value that occurs most frequently in fruits.
fruits.mode()
#or
fvc = fruits.value_counts()
fvc.head(1)

#10. Determine the string value that occurs leasr frequently in fruits.
fvc.tail(1)

#---------- EXERCISES PART II ----------
#1. Capitalize all the string values in fruits.
fruits.str.capitalize()

#2. Count the letter 'a' in all the string values (use string vectorization)
fsc = fruits.str.count('a')
print(fsc)
print('Total:', sum(fsc))

#3. Output the number of vowels in each and every string value.
fruits.str.count('[aeiou]')

#4. Write the code to get the longest string value from fruits.
fruits.str.len().max()

#5. Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() >= 5]

#6. Use the .apply method with a lamdba function to find the fruit(s) containg the
# containing the letter 'o' two or more times.
fruits[fruits.apply(lambda x: x.count('o') >= 2)]

#7. Write the code to get only the string values containing the substring 'berry'.
fruits[fruits.str.contains('berry')]

#8.  Write the code to get only the string values containing the substring 'apple'.
fruits[fruits.str.contains('apple')]

#9. Which string value contains the most vowels?
fruits[fruits.str.count('[aeiou]').max()]

#---------- EXERCISES PART III -----------
# Setup
raw_letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
letters = pd.Series(list(raw_letters))

#1. Which letter occurs the most frequently in the letters Series?
letters.value_counts().head(1)

#2. Which letter occurs the Least frequently?
letters.value_counts().tail(1)

#3. How many vowels are in the Series?
num_of_vow = letters.str.count('[aeiou]').sum()
print(num_of_vow)

#4. How many consonants are in the Series?
total_value = letters.value_counts().sum()
total_vow  = letters.str.count('[aeiou]').sum()
total_con = total_value - total_vow
print(total_con)

#5. Create a Series that has all of the same letters but uppercased.
letters.str.upper()

#6. Create a barplot of the frequencies of the 6 most commonly occuring letters.
six_top = letters.value_counts().head(6)
six_top.plot.hist()

# Create a Series named 'numbers' from the following:
raw_numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
numbers = pd.Series(raw_numbers)

#1.  What is the data type of the numbers Series?
type(numbers[1])

#2. How many elements are in the number Series?
numbers.count()

#3. Perform the necessary manipulations by accessing Series attributes
# and methods to convert the numbers Series to a numeric data type.
no_comma_num = numbers.str.replace(',','')
clean_numbers = no_comma_num.str.replace('$','')
clean_numbers = clean_numbers.astype(float)
numbers = clean_numbers
print(numbers)

#4. Run the code to discover the maximum value from the Series.
max_num = numbers.max()
print(max_num)

#5. Run the code to discover the maximum value from the Series.
min_num = numbers.min()
print(min_num)

#6. What is the range of the values in the Series?
range_of_num = max_num - min_num
print(range_of_num)

#7. Bin the data into 4 equally sized intervals or bins and output how 
# many values fall into each bin.
numbers.value_counts(bins=4)

#8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
numbers.value_counts(bins=4).plot.hist()
# Create a series names 'exam_scores' from the following list.
raw_grades = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series(raw_grades)
exam_scores

#1. How many elements are in the exam_scores Series?
exam_scores.value_counts().sum()

#2. Run the code to discover the min, max, mean, and median scores for exam_scores.
exam_scores.min()
exam_scores.max()
exam_scores.mean()
exam_scores.median()

#3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_scores.plot.hist()
plt.title('All_Grades')
plt(show)
#4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, and add the same number of 
# points to every other score in the Series as well.
curve = 100 - exam_scores.max()
curved_grades = exam_scores+curve
curved_grades

#5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of 
# letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

#6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.