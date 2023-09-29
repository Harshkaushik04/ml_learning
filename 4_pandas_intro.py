import numpy as np
import pandas as pd
#help(pd.Series)
my_index=['USA','Canada','Mexico']
my_data=[1776,1867,1821]
my_ser=pd.Series(data=my_data)
print(type(my_ser))
print(my_ser)
my_ser=pd.Series(data=my_data,index=my_index)#we can also do my_ser=pd.Series(my_data,my_index)
print(my_ser)
print(my_ser[0])
print(my_ser['USA'])
ages={'Sam':5,'Frank':10,'Spike':7}
ages_ser=pd.Series(ages)
print(ages_ser)
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}
sales_q1=pd.Series(q1)
sales_q2=pd.Series(q2)
print(sales_q1/100)
print(sales_q2+sales_q1)
first_half=sales_q1.add(sales_q2,fill_value=0)
print(first_half)
print(first_half.dtype)
print(sales_q1.dtype)
