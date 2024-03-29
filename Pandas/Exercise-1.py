#Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.

import pandas as pd
arr=pd.Series([12,23,35,6,4,77,54,99],index=['a','b','c','d','e','f','g','h'])
print(arr)

