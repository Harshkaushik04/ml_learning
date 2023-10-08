import numpy as np
import pandas as pd
ser=pd.Series(['ok','nice','five','5'])
print(ser)
print(ser.str.upper()) #converts to upper
print(ser.str.isalpha())#checks if alpha
print(ser[ser.str.isalpha()]) #filtering only string ones
tech_finance=['GOOG,APPL,AMZN','JPM,BAC,GS']
tickers=pd.Series(tech_finance)
print(tickers)
print(tickers.str.split(','))
#'GOOG,APPL,AMZN' is a single string and not 3 seperate strings but list created after splitting has 3 seperate elements
print(tickers.str.split(',')[0][0])
print(tickers.str.split(',').str[0]) #returns 1st element of both lists
#advanced stuff:
print(tickers.str.split(',',expand=True))
messy_names=pd.Series(['andrew  ','bo;bo','   claire   '])
print(messy_names)
messy_names=messy_names.str.replace(';','')
messy_names=messy_names.str.replace(' ','') #alternate method is to use strip method
print(messy_names)
messy_names=pd.Series(['andrew  ','bo;bo','   claire   '])
#better method:
messy_names=messy_names.str.replace(';','').str.strip()
print(messy_names)
#1 more method(custom function)
def cleanup(name):#custom function are generally more effecient than str functions
    name = name.replace(";","")
    name = name.strip()
    name = name.capitalize()
    return name
messy_names=pd.Series(['andrew  ','bo;bo','   claire   '])
messy_names=messy_names.apply(cleanup)
print(messy_names)
