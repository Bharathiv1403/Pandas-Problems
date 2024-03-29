"""np.array([10, 20, 30, 40, 50]): This code creates a NumPy array 'np_array' containing a sequence of five integers: [10, 20, 30, 40, 50].
new_series = pd.Series(np_array): This line creates a new Pandas Series object 'new_series' from the NumPy array using the pd.Series() constructor. The resulting Series object will have the same values as the NumPy array, and the default index will be assigned to each element starting from 0 and increasing by 1 for each subsequent element."""

import pandas as pd
import numpy as np

np_array=np.array([10, 20, 30, 40, 50])
print("NumPy array ")
print(np_array)
print("Converted Pandas series:")
df=pd.Series(np_array)
print(df)