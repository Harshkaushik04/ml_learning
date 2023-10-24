#for linear regression, its importnat to seperately evaluate residuals
#referring to anscombe s' quartet:
#only 1 feature us there, so we did "simple linear regression", but we can see visually that its not very correct
#but how do we know that when we are dealing with multiple features because we cant see the discrepancy of fit visually
#=>how to do that for multiple features??=>residual errors
#make these 2 plots for checking whether linear regression was good for this problem or not:
#density vs residual plot:should be a normal distribution(mean=0,peak at 0)
#residual error(|y(true)-y(predicted)|) vs true y value:should be random, shouldnt corrospend to specific curve
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
df=pd.read_csv("Advertising.csv")
X=df.drop("sales",axis=1)
y=df["sales"]
L=np.linspace(10,90)/100
L_invert=1-L
performance=[]
for element in L:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=element, random_state=101)
    my_model = LinearRegression()
    my_model.fit(X_train, y_train)
    predictions = my_model.predict(X_test)
    performance_mean_absolute = mean_absolute_error(y_test, predictions)
    performance_mean_squared = mean_squared_error(y_test, predictions)
    root_mean_squared = performance_mean_squared ** (1 / 2)
    performance.append(performance_mean_absolute)
plt.scatter(L_invert,performance)
plt.show()


