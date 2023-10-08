import numpy as np
import pandas as pd
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print(pd.merge(registrations,logins,how='inner',on='name')) #merging registrations and logins using inner merge on the column name
#"on the column name" means that whichever element match inside name column, it gets taken

#in inner merge, order of dataframes taken doesnt matter- registrations,logins=logins,registrations
