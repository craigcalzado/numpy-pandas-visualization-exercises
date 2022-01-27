#---------- EXERCISES PART I ---------- 
#setup
from itertools import count
from operator import indexOf
from tkinter import N
import numpy as np
import pandas as pd

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
vowels = list('aeiou')
fruits.isin(vowels)