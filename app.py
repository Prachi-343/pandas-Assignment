import pandas as pd
import numpy as np

#series:

# sr=pd.Series([1,2,3,4])
# sr=pd.Series(np.arange(1,10))
# print(sr)

#Dataframe:

# df=pd.DataFrame(data=[[1,2,3],[4,5,6],[7,8,9]],index=["row1", "row2","row3"],columns=["column1","column2","column3"])
# print(df)

# df=pd.DataFrame(data=np.arange(1,33).reshape(8,4),index=["row1","row2","row3","row4","row5","row6","row7","row8"],columns=["column1","column2","column3","column4"])
# print(df)

# df=pd.DataFrame(data=np.random.randint(1,100,(8,4)),index=["row1","row2","row3","row4","row5","row6","row7","row8"],columns=["column1","column2","column3","column4"])
# print(df)

#Datatype:

# print(type(df))

#Head & Tail:

# print(df.head())

# print(df.tail())

# print(df.head(4))

# print(df.tail(3))

# Describe:

# print(df.describe())


#access the dataframe with columns:

# df=pd.DataFrame(data=np.random.randint(1,100,(8,4)),index=["row1","row2","row3","row4","row5","row6","row7","row8"],columns=["column1","column2","column3","column4"])
# print(df[["column1","column2","column3"]])
# print(type(df[["column1"]]))
# print(type(df["column1"]))

#access the dataframe with rows:

# print(df.loc[["row1","row2","row3"]])
# print(df.loc[["row1","row3"]])

#Index location:

# print(df.iloc[0:3,:2])
# print(df.iloc[0:3,:2].values)

# df.info()

#value count for series data:

# print(df["column1"].value_counts())
# print(df["column1"].unique())
# print(df["column1"].nunique())

#nan(not a number:

# df=pd.DataFrame(data=[[1,2,3],[4,np.nan,6]],index=["row1","row2"],columns=["col1","col2","col3"])
# # print(df)
# print(df.isnull()) 
# print(df.isnull().sum())  
# print(df.isna())
# print(df.isna().sum())

#DataFrame using Dictionary:

# dict={'a':[1,2,3],'b':[4,5,6]}
# df1=pd.DataFrame(dict)
# print(df1)

#File conversion and reading:

# df=pd.DataFrame(data=np.arange(1,33).reshape(8,4),index=["row1","row2","row3","row4","row5","row6","row7","row8"],columns=["column1","column2","column3","column4"])
# df.to_csv('test.csv')
# df.to_csv('test.csv',index=False)
# df1=pd.read_csv('test.csv')
# print(df1)


#Conversion into Excel:
