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

