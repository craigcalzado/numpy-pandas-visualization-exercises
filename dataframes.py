#setup
from distutils.core import setup
from pydoc import describe
from tkinter.tix import COLUMN
from pydataset import data
import pandas as pd
import numpy as np

# 1.
np.random.seed(111)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)
print(df)

# a. 
pass_eng = df.english > 70
df['passing_english'] = pass_eng
df

# b. 
df.sort_values(by = 'passing_english')
# the duplicates are sorted by highest grade

# c. 
df.sort_values(by = ['passing_english', 'name'])

# d.
df.sort_values(by = ['passing_english', 'english'])

# e. 
df.drop(columns=['passing_english'])
avg_grades = (df.math + df.english + df.reading) / 3
df['overall_grades'] = avg_grades
print(df)
#2. 
mpg = data('mpg')

# a. 
mpg.shape

# b. 
mpg.dtypes

# c. 
mpg.info()
mpg.describe()

# d.
mpg.rename(columns={'cty': 'city'})

# e. 
mpg.rename(columns={'hwy': 'highway'})

# f. 
mpg[mpg.cty > mpg.hwy]
# There are no vehicles with cty better then hwy

# g. 
mpg['milage_difference'] = mpg.hwy - mpg.cty
mpg

# h.
mpg.sort_values(by = ['milage_difference'], ascending=False).head(2)

# i.
#setup
from pydoc import describe
from tkinter.tix import COLUMN
from pydataset import data
import pandas as pd
import numpy as np

# 1.
np.random.seed(111)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)
print(df)

# a. 
pass_eng = df.english > 70
df['passing_english'] = pass_eng
df

# b. 
df.sort_values(by = 'passing_english')
# the duplicates are sorted by highest grade

# c. 
df.sort_values(by = ['passing_english', 'name'])

# d.
df.sort_values(by = ['passing_english', 'english'])

# e. 
df.drop(columns=['passing_english'])
avg_grades = (df.math + df.english + df.reading) / 3
df['overall_grades'] = avg_grades
print(df)
#2. 
mpg = data('mpg')

# a. 
mpg.shape

# b. 
mpg.dtypes

# c. 
mpg.info()
mpg.describe()

# d.
mpg.rename(columns={'cty': 'city'})

# e. 
mpg.rename(columns={'hwy': 'highway'})

# f. 
mpg[mpg.cty > mpg.hwy]
# There are no vehicles with cty better then hwy

# g. 
mpg.drop(['milage_difference'], axis=1, inplace=True)  # removed a typo column name
mpg['mileage_difference'] = mpg.hwy - mpg.cty
mpg

# h.
mpg.sort_values(by = ['mileage_difference'], ascending=False).head(2)

# i.
comp = mpg[mpg['class'] == 'compact']
# Lowest hwy milage
comp.sort_values(by = ['hwy'], ascending=True).head(1)
# Highest hwy mileage
comp.sort_values(by = ['hwy'], ascending=False).head(1)

# j. 
mpg.drop(['average_milage'], axis=1, inplace=True) # removed a typo column name
mpg['average_mileage'] = mpg[['cty', 'hwy']].mean(axis= 1)
mpg

# k. 
dodge = mpg[mpg['manufacturer'] == 'dodge']
dodge.sort_values(by = 'average_mileage', ascending=False).head(1)

# 3. setup
mam = data('Mammals')
mam

# a. 
mam.shape

# b. 
mam.dtypes

# c. 
mam.info()
mam.describe()