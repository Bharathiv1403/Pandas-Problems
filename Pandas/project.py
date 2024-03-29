import pandas as pd

data=pd.read_csv("datas.csv")
# print(data.shape)

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




# row_count = len(data)
# print(row_count)
# shape = data.shape 
# print(shape)


# df1 = data.iloc[:, 0:n].head(m)
# print(df1)

# for i in range(len(df1)):
#     print(i)
# print(df1)
# df=pd.DataFrame(df1)



