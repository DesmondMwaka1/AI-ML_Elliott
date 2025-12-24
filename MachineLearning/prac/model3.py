import pandas as pd
from matplotlib import pyplot as pl

df=pd.read_csv(r"MachineLearning/prac/income.csv")
print(df)

pl.scatter(df["ID"],df["Age"],marker="o")
pl.scatter(df["ID"],df["Annual Income"],marker="*")
pl.scatter(df["ID"],df["Spending Score(1-100)"],marker="x")
#pl.scatter(df["ID"],df[""])
pl.show()