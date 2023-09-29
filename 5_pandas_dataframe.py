import numpy as np
import pandas as pd
np.random.seed(101)
my_Data=np.random.randint(0,101,(4,3))
print(my_Data)
my_index=['CA','NY','AZ','TX']#index to be set for dataframe
my_columns=['JAN','FEB','MAR']#column to be set for dataframe
df=pd.DataFrame(my_Data) #provided no index or column, so default index and column are 0,1,2,...
print(df)
df=pd.DataFrame(my_Data,index=my_index,columns=my_columns) #index and column specified as list
print(df)
#df.info()
#reading csv file-comma seperated value file
pd.set_option('display.max_columns',None)#command for displaying all columns
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/tips.csv') #reading csv file and storing it into a variable
print(df)
print(df.columns) #column list
print(df.index)#index list
print(df.head(5)) #first 5
print(df.tail(5))
df.info()
print(df.describe()) #gives basic info
#25 percent-split off data
#50 percent value=median
#print(df.describe().transpose()) #transpose==index to column and vice versa
#use include='all' inside argument of describe for including all index.

