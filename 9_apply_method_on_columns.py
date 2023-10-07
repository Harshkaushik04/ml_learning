import random
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None) #command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it inside variable
print(df.info()) #found that CC Number is int
#using apply method(first define function and then use it)
def last_four(num):
    return str(num)[-4:]
print(df['CC Number'].apply(last_four)) #not calling function by ourself, pandas is doinging it for us
print("wow:")
ok=int(input("Enter a number:"))
number=0
for i in range(ok):
    x=str(random.randint(1000,9999))
    wow=df[df['CC Number'].apply(last_four)==x]
    if len(wow)>0:
        number+=1
print(number/ok*100)
print(df.describe())
print(df['total_bill'].mean())
def finding_price_tag(num):
    if num<20:
        return "$"
    elif num<25:
        return "$$"
    elif num<40:
        return "$$$"
    else:
        return "$$$$"
price_tagging=df['total_bill'].apply(finding_price_tag)
print(price_tagging)
print(price_tagging.describe())
#for calculating frequency
#value_counts method replaces this function
def frequency(series):
    d={}
    for x in series:
        d[x]=d.get(x,0)+1
    return d
print(frequency(price_tagging))
