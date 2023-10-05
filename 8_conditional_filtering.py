#columns are features
# df[df["pop">50]]-conditional filtering
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None) #command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it inside variable
print(df.head())
#give rows where total_bill>40
bool_series=df["total_bill"]>40 #bool series of true and false arranged in order of index
print(df[bool_series]) #could be done in 1 line
#give rows where sex is male
print(df[df["sex"]=="Male"])
#multiple conditions filtering
# & --- both conditions to be true
# | --- either of conditions to be true
print(df[(df["total_bill"]>40) & (df["sex"]=="Male")])
print(df[(df["total_bill"]>40) | (df["sex"]=="Male")])
#for mutiple condition filtering easeir method is isin method[is in]
options=['Sun','Sat','Fri'] #multiple options appended into list
print(df[df["day"].isin(options)])