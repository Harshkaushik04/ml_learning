import pandas as pd
#link in jupyter notebook for commands to open different type of files
import os #for finding location
print(os.getcwd()) #finding location
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/example.csv',index_col=0) #setting index as 1st column
print(df)
df.to_csv('newfile.csv') #creating new file+location of df
new=pd.read_csv('newfile.csv')
print(new)
df.to_csv('new.csv',index=False)#index is removed(basically 0,4,8,12) column is removed
new_2=pd.read_csv('new.csv')
print(new_2)