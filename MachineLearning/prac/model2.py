import pandas as pd
from matplotlib import pyplot as pl

df=pd.read_csv(r"MachineLearning/prac/hospital.csv")
print(df)

"""pl.scatter(df["ID"],df["Age"])
pl.plot(df["ID"],df["Sick"])
pl.show()
"""
