#outer merge allows to keep values of all dataframe
import numpy as np
import pandas as pd
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print(pd.merge(registrations,logins,how='outer',on='name'))
#in outer merge too, order doesnt matter
#more advanced things in combining databases
#4 more things which we can do in merge:
#left_on,right_on,left_index,right_index
registrations=registrations.set_index('name')
adv=pd.merge(registrations,logins,left_index=True,right_on='name',how='inner') #take left(registrations) s' index as merging point and 'name' column from logins as other merging point
print(adv)
registrations=registrations.reset_index()
registrations.columns=['reg_name','reg_id']
adv_2=pd.merge(registrations,logins,left_on='reg_name',right_on='name',how='inner')
print(adv_2)
adv_2=adv_2.drop('name',axis=1) #dropping 'name' column because reg_name column was already there
print(adv_2)
registrations.columns=['name','id']
logins.columns=['id','name']
print(pd.merge(registrations,logins,left_on='name',right_on='name',how='inner')) #doing this, id_x and id_y columns would be formed as both registrations and logins contain column for id, we can change value of x and y by using suffixes
print(pd.merge(registrations,logins,how='inner',left_on='name',right_on='name',suffixes=('_reg','_log')))
