import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv("Advertising.csv")
X=df.drop("sales",axis=1)
y=df["sales"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)
from sklearn.linear_model import LinearRegression
my_model=LinearRegression()
my_model.fit(X_train,y_train)
my_predictions=my_model.predict(X_test)
from sklearn.metrics import mean_absolute_error,mean_squared_error
absolute_error=mean_absolute_error(y_test,my_predictions)
root_mean_squared_error=np.sqrt(mean_squared_error(y_test,my_predictions))
print(absolute_error)
print(root_mean_squared_error)
plt.scatter(y_test,y_test-my_predictions,color='blue')
plt.xlabel("true value")
plt.ylabel("residual error")
plt.axhline(y=0,color='black',ls='--')
plt.show()
sns.displot(y_test-my_predictions,bins=25,kde=True) #comapare this to normal distribution
plt.show()
#comaparing our plot to ideal normal distribution
'''
import scipy as sp
# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(6,8),dpi=100)
# probplot returns the raw values if needed
# we just want to see the plot, so we assign these values to _
_ = sp.stats.probplot((y-my_predictions),plot=ax)
plt.show()
#copied from jupyter notebook
'''
final_model=LinearRegression()
final_model.fit(X,y)
print(final_model.coef_)#coeffecients for linear regression
y_hat=final_model.predict(X)
fig,axes = plt.subplots(nrows=1,ncols=3,figsize=(16,6))

axes[0].plot(df['TV'],df['sales'],'o')
axes[0].plot(df['TV'],y_hat,'o',color='red')
axes[0].set_ylabel("Sales")
axes[0].set_title("TV Spend")

axes[1].plot(df['radio'],df['sales'],'o')
axes[1].plot(df['radio'],y_hat,'o',color='red')
axes[1].set_title("Radio Spend")
axes[1].set_ylabel("Sales")

axes[2].plot(df['newspaper'],df['sales'],'o')
axes[2].plot(df['radio'],y_hat,'o',color='red')
axes[2].set_title("Newspaper Spend")
axes[2].set_ylabel("Sales")
plt.tight_layout()
plt.show()
#from jupyter notebook
from joblib import dump,load #for saving the model
dump(final_model,'final_sales_model.joblib')
loaded_model=load('final_sales_model.joblib')
print(loaded_model.coef_)
#predict sales during compaign1(149 TV 22 Radio 12 Newspaper),compaign2(22Radio 149 Radio 12 Newspaper)
print(X.shape)
compaign1_2=[[149,22,12],[22,149,12]]
print(loaded_model.predict(compaign1_2))