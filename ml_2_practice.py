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
L=np.linspace(10,50)/100
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

