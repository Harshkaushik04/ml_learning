import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None) #command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it inside variable
print(df.index) #default index is this
print(df)
#lets modify index setting(acc to column)
df=df.set_index('Payment ID') #this change is not permanent if we dont equate it to variable
#now,Payment ID is not a column but is index
print(df)
#df=df.set_index("price_per_person") #if we do this, Payment ID will disapper as it was not column but index
#print(df)
df=df.reset_index()#resets index and equating to variable for making change permanent
print(df)
df=df.set_index('Payment ID')
print(df)
print(df.iloc[0]) #picking 1st row as index
print(df.loc['Sun2959']) #picking 1st row as labelled index
#picking multiple rows
print(df.iloc[:4]) #using slicing method
print(df.iloc[[0,1,2,3]])
print(df.loc[['Sun4458','Sun5260']])
#deleting/dropping or inserting row
df=df.drop('Sun4458',axis=0) #df.drop(0,axis=0) is wrong because you have labelled index
one_row=df.iloc[0]
print(one_row)
df=df._append(one_row)
print(df)
df=df.reset_index()
print(df)
