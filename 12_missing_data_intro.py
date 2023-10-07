#methods to deal with missing data:
#1.keep it(cons:some ml methods dont allow missing data)
#2.remove it(cons:might lose important feature)
#3.replace it(cons:needs reasonable assumption to do and is hard)
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None)
#wrong method
print(np.nan==np.nan) # =>false, because we dont know value of missing data
print(np.nan is np.nan)
my_var=np.nan
print(my_var is np.nan) #to check whether my_var is np.nan
df=pd.read_csv('/home/harsh/ml_zip_files_unzipped/03-Pandas/movie_scores.csv')
print(df)
print(df.isnull())#to check null values
print(df.notnull())#to check not null values
not_null=df.notnull()
print(df[not_null['pre_movie_score']==True]) #data for which pre_movie_Score doesnt have any null value
#alternate method:
print(df[df['pre_movie_score'].notnull()])
print(df[(df['pre_movie_score'].notnull()) & (df['sex'].notnull())]) #data for which both pre_movie_score and sex doesnt have null value
#print(help(df.dropna))
#by default,axis=0
print(df.dropna()) #drops rows which have even 1 null value
print(df.dropna(thresh=1)) #atleast 1 non null values
print(df.dropna(thresh=5)) #atleast 5 non null values
df.dropna(axis=1) #drops column which have even 1 null value => df gets totally erased as all its columns conmtain atleast 1 null value
#subset
print(df.dropna(subset=['last_name'])) #checks only subset of particular columns
print(df.dropna(subset=['last_name','pre_movie_score']))
print(df)
#filling data
#print(df.fillna("NEW VALUE!")) #all null values gets replaced by it
#if you fill string(like-"NEW VALUE!" in a column having int, those int gets converted to string
print(df['pre_movie_score'].fillna(df['pre_movie_score'].mean())) #mean method doesnt mind null values
#df.fillna(df.mean())#for every null value, fills it with mean value of that column => not working??
subset=['pre_movie_score','post_movie_score']
df[subset]=df[subset].fillna(df[subset].mean())
print(df)