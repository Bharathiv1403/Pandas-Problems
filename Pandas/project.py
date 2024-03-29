"""In the above example :
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}: This line creates a Python dictionary 'd1' with five key-value pairs. Each key is a string ('a', 'b', 'c', 'd', 'e') and each value is an integer.
new_series = pd.Series(d1): This line creates a new Pandas Series object 'new_series' from the dictionary 'd1' using the pd.Series() constructor. The resulting Series object will have the same keys as the dictionary and the corresponding values as its elements."""

import pandas as pd
data=pd.read_csv("datas.csv")

start=0
col_end=5

row_start=0
row_end=10

for _ in range ((len(data.axes[0])+1)//10):
    for _ in range((len(data.columns))//5):
        df=pd.DataFrame(data.iloc[row_start:row_end,start:col_end])
        print(df.to_string())

        start+=5
        col_end=+5

    start=0
    col_end=5

    row_start+=10
    row_end+=10

    print("**************************************************************************************************** \n ****************************************************************************************************")
