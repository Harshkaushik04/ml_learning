#simple linear regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sympy
import math
df=pd.read_csv("Advertising.csv")
df['total_spent']=df['TV']+df['radio']+df['newspaper']
print(df.head())
#to find relation between total_spent and sales
#plt.scatter(df['total_spent'],df['sales'],color='black')
#plt.show()
#sns.scatterplot(data=df,x='total_spent',y='sales')
#sns.regplot(data=df,y='sales',x='total_spent') #=>line of best fit
#plt.show()
X=df['total_spent']
y=df['sales']
coefficients=np.polyfit(X, y, deg=1) #=>in y=(b1)x+b0 matrix is [b1 b0] is printed
potential_spent=np.linspace(0,500,100)
predicted_Sales=coefficients[0]*potential_spent+coefficients[1]
plt.scatter(X,y,color='blue')
plt.plot(potential_spent,predicted_Sales,color='black')
plt.title("Linear curve fit")
plt.xlabel("spent")
plt.ylabel("sales")
plt.show()
spent=200
predicted_sales=coefficients[0]*spent+coefficients[1]
print(predicted_sales)
playing_around_with_cubic=np.polyfit(X,y,deg=3)
predicted_sales_two=[]
for j in range(len(potential_spent)):
    sum = 0
    for i in range(len(playing_around_with_cubic)):
        sum+=playing_around_with_cubic[i]*math.pow(potential_spent[j],3-i)
    predicted_sales_two.append(sum)
plt.plot(potential_spent,predicted_sales_two,color='black')
plt.scatter(X,y,color='blue')
plt.title("cubic curve fit")
plt.xlabel("spent")
plt.ylabel("sales")
plt.show()
#linear curve fit vs cubic curve fit gave the idea of whether which is better=>to calculate from performance matrix