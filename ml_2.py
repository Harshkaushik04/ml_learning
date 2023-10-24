import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv("Advertising.csv")
print(df.head())
'''
fig,axes = plt.subplots(nrows=1,ncols=3,figsize=(16,6))
axes[0].plot(df['TV'],df['sales'],'o')
axes[0].set_ylabel("Sales")
axes[0].set_title("TV Spend")

axes[1].plot(df['radio'],df['sales'],'o')
axes[1].set_title("Radio Spend")
axes[1].set_ylabel("Sales")

axes[2].plot(df['newspaper'],df['sales'],'o')
axes[2].set_title("Newspaper Spend");
axes[2].set_ylabel("Sales")
plt.tight_layout()
plt.show()

sns.pairplot(df)
plt.show()
'''
X=df.drop("sales",axis=1)
print(X.head())
y=df["sales"]
print(y.head())
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)
'''
print(len(df))
print(len(X_train))
print(X_train.head())
'''
from sklearn.linear_model import LinearRegression
#help(LinearRegression)
my_model=LinearRegression()
my_model.fit(X_train,y_train)
predictions=my_model.predict(X_test)
# 3 types of error matrices we can make for linear regression task
#1. mean absolute error
#2. mean squared error
#3. root mean squared error
from sklearn.metrics import mean_absolute_error,mean_squared_error
performance_mean_absolute=mean_absolute_error(y_test,predictions)
performance_mean_squared=mean_squa red_error(y_test,predictions)
root_mean_squared=performance_mean_squared**(1/2)
print(performance_mean_absolute)
print(root_mean_squared)