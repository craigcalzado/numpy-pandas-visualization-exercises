#---------- EXERCISES PART I ---------- 
#setup
from itertools import count
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
fruits.str.count('[aeiou]')

#4. Write the code to get the longest string value from fruits.
max(fruits.str.count('[a-z]'))

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




