#outer merge allows to keep values of all dataframe
import numpy as np
import pandas as pd
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print(pd.merge(registrations,logins,how='outer',on='name'))