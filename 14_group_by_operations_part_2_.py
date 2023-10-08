import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None)
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/mpg.csv')
updated_columns=['mpg','displacement','weight','acceleration','origin']
#to grab cross section, we use .xs method
year_cyl=df.groupby(['model_year','cylinders'])[updated_columns].mean()
print(year_cyl.xs(key=70,level='model_year')) #alternatively we can use year_cyl.loc[70]
four_cylinder=year_cyl.xs(key=4,level='cylinders') #output is all rows corrosponding to each year s' 4 cylinder column
print(four_cylinder) #named variable so ,because it would be confusing if didnt in this case
print(df[df['cylinders'].isin([6,8])].groupby(['model_year','cylinders'])[updated_columns].describe())
#grouping data of 6 and 8 cylinders only
print(year_cyl.swaplevel()) #swaps the levels
print(year_cyl.sort_index(level='model_year',ascending=False))
#aggregate function
print(df[updated_columns+['model_year']].agg(['std','mean'])) #standard deviation and mean of df columns
print(df.agg({'mpg':['max','mean'],'weight':['mean','std']})) #doing different methods with different columns