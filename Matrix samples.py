import numpy as np
import pandas as pd

arr = np.arange(0, 25)
arr_2d = arr.reshape(5, 5)
print(arr)
print (arr_2d)

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]

pd.Series(data=my_data, index=labels)

print(pd.Series)



