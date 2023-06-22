import pandas as pd
import numpy as np

# ----------Pandas Dataframe------------



# Crating Dataframe using a single list

# a = ['Mitesh','Aayush','Naresh','Pratham','Umedsingh']
#
# df = pd.DataFrame(a)
# print(df)
#




# Creating DataFrame from dict of ndarray/lists

# Note : all the narray must be of same length.

# data = {'ID':['1126','1102','1203','1127','1024'],'Name':['Mitesh','Naresh','Pratham','Umed','Ratan']}
#
# dataf = pd.DataFrame(data)
# print(dataf)


# Dealing With Rowa and Columns

# Column Selection

# data1 = {'Name':['Mitesh','Umed','Pratham','Naresh'],
#          'Age' : ['20','20','17','23'],
#          'City' : ['Ahmedabad','Gandhinagar','Ahmedabad','Jaipur'],
#          'Qualification' : ['B.Tech','B.tech','Diploma(CE)','Bsc. Nursing']
#          }
#
# df = pd.DataFrame(data1)
#
# print(df[['Name','Qualification']])


#-----Pandas Series----


# Empty Series


# ser = pd.Series()
#
# print(ser)

#
# # Creating Series using np.array
#
# d1 = np.array(['Mitesh','Umed','Naresh'])
#
# ser1 = pd.Series(d1)
#
# print(ser1)
#
# print()
#
# # series with index
#
#
# ser2 = pd.Series(d1,index=[10,11,12])
#
# print(ser2)
#
# # Series using list
#
# list = ['M','I','T','E','S','H']
#
# seri = pd.Series(list)
#
# print(seri)
#
# # Series using dict
#
# dict = {'Name':'Mitesh',
#         'Age': '20',
#         'Cource' : 'B.tech'
#         }
#
# ser3 = pd.Series(dict)
#
# print(ser3)
#
# # Creating a series from Scalar value
#
# series1 = pd.Series(10,index=[0,1,2,3,4,5])
#
# print(series1)



# Creating a series using NumPy functions :
#
# ch = pd.Series(np.linspace(1,20,5))
# print(ch)
#
# # series using range()
#
# ra = pd.Series(range(10))
#
# print(ra)
#
# # series using for loop
#
# fo  = pd.Series(range(1,20,3),index=[x for x in 'abcdefg'])
# print(fo)
#
# # Creating a Series using mathematical expressions:
#
# ad = np.arange(10,15)
#
# sed = pd.Series(data=ad*3,index=ad)
#
# print(sed)

# csvv = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
#
# # data_top = csvv.head(9)
# #
# # print(data_top)
#
# sr = csvv["Name"]
#
# m = 5
#
# top = sr.head(n= m)
# print(top)
# print()
# print()
# data_bottom = csvv.tail()
#
# print(data_bottom)
#
#
# sd = csvv[["Name","Salary"]]
#
# bottom = sd.tail(n=7)
#
# print(bottom)


# --Pandas describe() behavior for numeric dtypes--

# data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
#
# # removing null values to avoid errors
# data.dropna(inplace=True)
#
# perc = [.20,.40,.60,.80]
#
# include = ['int','float','object']
#
# desc = data.describe(percentiles=perc,include=include)
# print(desc)
#
# desc1 = data["Name"].describe()
#
# print(desc1)


# -----Convert dataframe to Numpy array------

# df = pd.DataFrame(
#
#     [[1,2,3],
#      [4,5,6],
#      [7,8,9]],
#     columns=['a','b','c']
# )
#
# arr = df.to_numpy()
#
# print("\n DataFrame : \n",df)
#
# print("\n\n Numpy Array : \n ",arr)
#
# # want to convert a particular column into numpy array.
#
# p_arr = df[['a','c']].to_numpy()
# print()
# print(p_arr)
#
# sr = pd.read_csv("nba.csv")
#
# sr.dropna(inplace=True)
#
# gfg = pd.Series(sr["Name"].head())
#
#
#
# print(gfg)
# print(type(gfg))
#
# print()
# n = gfg.to_numpy()
# print(n)
# print(type(n))

#
# sr = pd.Series([1,2,3,4,5,6,7,8,9])
#
# index_ = ['0','1','2','3','4','5','6','7','8']
#
# sr.index = index_
#
# print("\n DataFrame : \n",sr)
# print(type(sr))

# mat = df.as_matrix()
# result = sr.as_matrix()                                   # has been deprecated
# print("\n\n Numpy Array : \n ",result)
# print(type(result))




# ---------Dealing with Rows and Columns in Pandas DataFrame--------

# Dealing with Columns

    # Column Selection


# data_csv = pd.read_csv("xyz.csv")
#
# df = pd.DataFrame(data_csv)
#
# print(df[['Name','Hobby']])



# Column Adddition

# data_csv = pd.read_csv("xyz.csv")
#
# df = pd.DataFrame(data_csv.head())
#
# print("\n DataFrame Before adding any column : \n\n",df)
#
# add = ['Ahmedabad','Gandhinagar','Gota','Jaipur','Deldar']
#
# df['Address'] = add
#
# print("\n\n DataFrame after adding address colummn : \n\n ",df)
#
#
#
# # Those values were dropped since axis was set equal to 1 and the changes were made in the original data frame since inplace was True.
# df.drop(['Address'],axis=1,inplace=True)
#
# print("\n\n DataFrame after droppig address column : \n\n",df)


# -----Dealing With Rows---

# data = pd.read_csv("xyz.csv",index_col="Name")
#
# # first = data.loc["Mitesh"]
# # sec = data.loc["Umed"]
# r = data.loc[["Mitesh","Umed"]]
# print(f" \n\n {r}")
#
# print("\n\nDataFrame before adding extra row : \n\n",data.head(5))
#
# new_row = pd.DataFrame({'Name':'MJ','Age':'25','Hobby':'Dance'},index=[0])
#
# # df = pd.concat([new_row,data]).reset_index(drop=True)
# #
# # print(df)
#
# v = data.drop(["Mitesh"],inplace=True)
# print("\n\nDataFrame after deleting a row : \n\n",data.head(5))


#  Extracting multiple rows with same index

# data = pd.read_csv("xyz.csv",index_col="Age")
# rows = data.loc[[20,21]]

# Extracting data from a range of rows
#
# data = pd.read_csv("xyz.csv",index_col="Name")
# rows = data.loc["Mitesh":"Naresh"]
# print(rows)



# data = pd.read_csv("nba.csv")
#
# row1 = data.loc[3]
#
# row2 = data.iloc[3]
#
# print(row1 == row2)
#
#
# row1 = data.iloc[[4,5,6,7]]
#
# row2 = data.iloc[4:8]
#
# print(row1 == row2)

# data = pd.read_csv("nba.csv")
#
# print("Slicing only rows till 4 : \n\n")
# x1 = data.ix[:4,]                                      # .ix is deprecated
# print(x1)
# print("Slicing  rows(till 4 , column 1-4 excluding 4) : \n\n")
# x2 = data.ix[:4,1:4]
# print(x2)



# data = pd.read_csv("nba.csv",index_col="Name")
#
# # row1 = data.loc["Amir Johnson"]
# # df = pd.DataFrame(row1)
# # print(df[["Name","Age","College","Salary"]])
# # print(df
# #       )
# fri = data.iloc[[5,8],[3,6,7]]
# print(fri)
#
# asd = data.iloc[[2,5,8]]
# print(asd)
#
# ads = data.iloc[:,[3,4,7]]
# print(ads)


# Adding new column to existing DataFrame in Pandas


# data_csv = pd.read_csv("xyz.csv")
#
# df = pd.DataFrame(data_csv.head())
#
# print("\n DataFrame Before adding any column : \n\n",df)
#
# add = ['Ahmedabad','Gandhinagar','Gota','Jaipur','Deldar']
#
# # df['Address'] = add
#
# # print("\n\n DataFrame after adding address colummn : \n\n ",df)
# #
# # v = df.insert(2,"Address",['Ahmedabad','Gandhinagar','Gota','Jaipur','Deldar'],True)                # Using insert method
# #
# # print("\n\n DataFrame after adding address colummn : \n\n ",df)
# #
#
# df1 = df.assign(address =['Ahmedabad','Gandhinagar','Gota','Jaipur','Deldar'] )     # made new dataframe with new column
#
# print("\n\n",df1)
#
# data = pd.read_csv("nba.csv",index_col="Name")

# data.drop(["Avery Bradley","R.J. Hunter","John Holland"],inplace=True)
# print(data)

data = pd.read_csv("nba.csv")
#
# for i,j in data.iterrows():
#     print(i,j)
#     print()
#
# for key,value in data.iteritems():                                                  # iteritems() has been deprecated
#     print(key,value)
#     print()

# for i in data.itertuples():
#     print(i)
#     print()