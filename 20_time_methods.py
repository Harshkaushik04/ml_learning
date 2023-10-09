import numpy as np
import pandas as pd
from datetime import datetime
my_year=2015
my_month=1
my_day=1
my_hour=2
my_min=30
my_sec=15
my_date=datetime(my_year,my_month,my_day,my_hour,my_min,my_sec) #descending order
print(my_date)
my_ser=pd.Series(['Nov 3,1990','2001-01-01',None])
print(my_ser)
time_ser=pd.to_datetime(my_ser)#converts everything into date time
print(time_ser)
print(time_ser[0].year)
obvi_euro_Date='31-12-2000' #obvious that 31 is date and 12 is month
print(pd.to_datetime(obvi_euro_Date))
euro_date='10-12-2000' #acc to american 12 is date
print(pd.to_datetime(euro_date)) #assumes 12 to be date
print(pd.to_datetime(euro_date,dayfirst=True)) #set day as first
style_date='12--dec--2000'
print(pd.to_datetime(style_date,format='%d--%b--%Y')) #writing format for clarification to program
# %d-for day, %b-for month, %Y for year
custom_date='12th of dec 1990'
print(pd.to_datetime(custom_date))
sales=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/RetailSales_BeerWineLiquor.csv')
print(sales)
print(sales['DATE'])
sales['DATE']=pd.to_datetime(sales['DATE']) #convert from object datatype to datetime datatype
print(sales['DATE'])
print(sales['DATE'][0].year)
sales=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/RetailSales_BeerWineLiquor.csv',parse_dates=['DATE'])
print(sales['DATE'])
sales=sales.set_index('DATE') #set index at DATE column
print(sales)
sales=sales.resample(rule='A').mean() #its likegroupby method of grouping/classifying data, basically for datetime datatype
#rule='A' means group it by year(all the rule paramters link given in jupyter notebook of time methods
print(sales)
sales=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/RetailSales_BeerWineLiquor.csv',parse_dates=['DATE'])
print(sales.info())
print(sales['DATE'].dt.year) #dt here stands for calling method from datetime library
#gives series of years