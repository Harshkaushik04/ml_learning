import numpy as np
import pandas as pd
data_one = {'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}
one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)
#concatinating along columns
print(pd.concat([one,two],axis=1))
#concatinating along row
print(pd.concat([one,two],axis=0))
two.columns=one.columns #convert two s' column names into one s' to match up column names
concatenated_df=pd.concat([one,two],axis=0)
concatenated_df.index=range(8)
print(concatenated_df)