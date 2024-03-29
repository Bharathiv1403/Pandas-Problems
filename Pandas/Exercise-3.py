"""Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]"""

import pandas as pd
a=pd.Series([2, 4, 6, 8, 10])
b=pd.Series([1, 3, 5, 7, 9])

print("Add two Series")
df=a+b
print(df)

print("Subtract two Series")
df1=a-b
print(df1)

print("Multiple two Series")
df2=a*b
print(df2)

print("Divide Two Series")
df3=a/b
print(df3)

