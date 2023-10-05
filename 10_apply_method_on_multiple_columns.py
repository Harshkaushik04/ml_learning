import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None) #command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it inside variable
#value_counts() method replaces this function
def frequency(series):
    d={}
    for x in series:
        d[x]=d.get(x,0)+1
    return d
#for applying (apply method) on multiple columns we need to learn lambda expression
#simple function:
def simple(num):
    return num*2
# =>conversion to lambda expression:
# lambda num:num*2
print(df['total_bill'].apply(lambda num:num*2)) #using lambda expression
df['tip/bill']=df['tip']/df['total_bill']
print(df['tip/bill'].describe())
def tip_to_bill_ratio(tip,bill):
    if tip/bill<0.1:
        return "low"
    elif tip/bill<0.15:
        return "average"
    elif tip/bill<0.2:
        return "decent"
    else:
        return "really good"
df['quality']=df[['tip','total_bill']].apply(lambda df:tip_to_bill_ratio(df['tip'],df['total_bill']),axis=1) #axis=1 is a secondary argument
#3 components:
#1.columns to be selected
#2.lambda expression
#3.custom function to design(in this case, tip_to_bill_ratio
print(df['quality'])
print(frequency(df['quality']))
#effecient method:
#2 componenets:
#1. custom function
#2. columns selected
df['quality']=np.vectorize(tip_to_bill_ratio)(df['tip'],df['total_bill'])
print(df['quality'])
