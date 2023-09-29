import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None) #command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it inside variable
print(df)
print(df.head(5)) #printing first 5 index
print(df['total_bill']) #each of the column is a panda series
print(type(df['total_bill']))
print(df['total_bill',])
