import numpy as np
import pandas as pd
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print(registrations)
print(logins)
print(pd.merge(registrations,logins,how='left',on='name'))
#all the elements in left dataframe(registrations) of name column,show up
#as charlie and david are not present in logins dataframe, hence value is nan
print(pd.merge(registrations,logins,how='right',on='name'))
print(pd.concat([registrations,logins],axis=1)) #concatenation