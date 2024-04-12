import pandas as pd
df = pd.read_csv("sen.csv")
df['DOB'] = pd.to_datetime(df['DOB']).dt.date
print(df.to_string())
df.to_csv('Bharathi.csv')













# import pandas as pd
# df=pd.read_csv("sen.csv")


# data=df.iloc[:, [(clm == 'DOB') | (0 in df[clm].unique()) for clm in df.columns]]
# print(data.head(50).to_string())
# sen=data.drop("00:00:00")
# print(sen.head(10))




# data = pd.DataFrame(clm).dt.date
# print(data.head(50).to_string())
# sen = data.drop("00:00:00", axis=0, errors='ignore')
# print(sen.head(10))


# import pandas as pd
# df = pd.read_csv("sen.csv")
# df['DOB'] = pd.to_datetime(df['DOB']).dt.date
# print(data.head(50).to_string())












# print(data)
# for i in data:
#     if i == "00:00:00":
#         pass
#     else:
#         print(i)