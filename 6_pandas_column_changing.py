import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None) #command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it inside variable
print(df)
print(df.head(5)) #printing first 5 index
print(df['total_bill']) #each of the column is a panda series
print(type(df['total_bill']))
print(df[['total_bill','tip']]) #or alpha=['total_bill','tip'] => df[alpha]
timepass=df['tip']+df['total_bill']
print(timepass)
df['tip_percentage']=np.round(df['tip']/df['total_bill']*100,decimals=2) #creating new column inside df
#np.round(  ,decimels= ) rounds off to 2 decimal places
print(df)
#for deleting/dropping a row/column, use df.drop()
#this drop functionality is temporary means df gets original after that line.
#to make this permanent either store it in another variable or same(can also use implace-but 1st method is better)
temporary_df=df.drop('tip_percentage',axis=1)
print(temporary_df)
print(df)
df=df.drop('tip_percentage',axis=1)
print(df)
