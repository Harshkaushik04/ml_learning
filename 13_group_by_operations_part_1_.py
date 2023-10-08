#groupby() allows to examine data as per category basis
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None)
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/mpg.csv')
print(df)
print(df['model_year'].value_counts())
columns=['mpg','cylinders','displacement','weight','acceleration','origin'] #columns which i want
print(df.groupby('model_year')[columns].mean())#grouping data on basis of model_year and then calculating mean of all columns listed in the list (columns)
#multi level grouping:
updated_columns=['mpg','displacement','weight','acceleration','origin']
print(df.groupby(['model_year','cylinders'])[updated_columns].mean())
print(df.groupby(['model_year','cylinders'])[updated_columns].mean().index) #multi index
print(df.groupby('model_year').describe()) #multiple paramters on all columns
column=list(df.columns)
index=list(df.index)
print(column)
year_cyl=df.groupby(['model_year','cylinders'])[updated_columns].mean() #mean paramter on updated_columns with multi index as model_year and cylinders
print(year_cyl)
print(year_cyl.index.names) #components of multi index
print(year_cyl.index.levels) #list of both levels of multi index
print(year_cyl.loc[70]) #70 is outer index
print(year_cyl.loc[70,6]) #specific index
print(year_cyl.loc[(70,6)]) #can also pass tuple for same purpose as before