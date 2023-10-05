import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None) #command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it inside variable
print(df.describe())
df=df.sort_values('tip',ascending=False) #sorts in descending order
df=df.sort_values(['tip','size']) #sortes from priority tip to size(tip and size)
print(df)
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reseting
df=df.set_index('CC Number')
print(df['total_bill'].idxmax()) #index of max in total_bill
index_of_max=df['total_bill'].idxmax() #index of max
print(df.loc[index_of_max]) #finding details of max by generating row
#correlation of columns
#print(df.corr()) => why not working??
print(df['sex'].value_counts()) #for frequency of each
#for finding list of unique elements:
print(df['sex'].unique())
print(df['sex'].nunique()) #for number of unique elements
#replacing by list
df['sex']=df['sex'].replace(['Male','Female'],['M','F']) #list of elements to replace and also what to replace to
print(df['sex'])
print(df)
#replacing by dictionary(mapping)
my_map={'Female':'F','Male':'M'}
df['sex']=df['sex'].map(my_map)
print(df)

