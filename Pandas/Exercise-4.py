"""Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]"""

import pandas as pd 
df1=pd. Series([2, 4, 6, 8, 10])
df2=pd.Series([1, 3, 5, 7, 10])

# print("First Series")
# print(df1)

# print("Sencond Series")
# print(df2)

# print("Two Series Comapar")
# df=df1 == df2
# print(df)

# print("Lessthan Series")
# dl= df1 < df2
# print(dl)

# print("Greater than Series")
# dg= df1 > df2
# print(dg)

# sr1 = pd.Series([2, -7, 6, 8, 10])
# sr2 = pd.Series([1, 3, 6, 7, 9])

sr1=pd. Series([2, 4, 6, 8, 10])
sr2=pd.Series([1, 3, 5, 7, 10])

print(sr1.lt(sr2));print("-"*50)
print(sr1.le(sr2));print("-"*50)
print(sr1.gt(sr2));print("-"*50)
print(sr1.ge(sr2));print("-"*50)
print(sr1.eq(sr2))