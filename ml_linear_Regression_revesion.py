import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv("Advertising.csv")
X=df.drop("sales",axis=1)
y=df["sales"]
