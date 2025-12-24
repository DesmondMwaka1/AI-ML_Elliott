import pandas as pd
from matplotlib import pyplot as pl
import sklearn
import sklearn.linear_model
import numpy as np
import sklearn.neighbors
import sklearn.tree

df=pd.read_csv(r"MachineLearning/prac/advSales.csv")
print(df)


x=np.c_[df["adv"]]
y=np.c_[df["Sales"]]



model=sklearn.linear_model.LinearRegression()

model.fit(x,y)

x_new=[[250]]
print(model.predict(x_new))

pl.scatter(x,y)
pl.show()

print(x)
print(y)