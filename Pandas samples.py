import numpy as np
from numpy.random import randn
import pandas as pd

np.random.seed(101)

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]

#--------------------------------------
# Panda Series
#--------------------------------------
pd.Series(data=my_data, index=labels)
# pd.Series(numpy array)
# pd.Series(dict)
ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'France', 'Japan'])
ser2 = pd.Series([1,2,3,4], ['USA', 'Germany', 'France', 'Japan'])
ser1 + ser2
ser1['USA']

#------------------------------------
# Panda DataFrames
#------------------------------------
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
df['W']   # column
df['X']   # column
df[['W'], ['X']]  # 2 columns
df['new'] = df['W'] + df['Y']  # adding a column
df.drop('E')
df.drop('E', axis=0)
df.shape
# column: axis = 1
# row: axis = 0
df.loc['A']  # row
df.iloc[2]   # 3rd row - 'C'

df.loc['B', 'Y']  # value 
df.loc[['A', 'B'], ['W', 'Y']]  # 4 values 

