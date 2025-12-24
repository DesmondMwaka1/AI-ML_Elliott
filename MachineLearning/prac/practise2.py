import pandas as pd
from matplotlib import pyplot as pl

df=pd.read_csv(r"MachineLearning/prac/couHappy.csv")

""" 
gdpMean=df["GDP"].mean()
satisMean=df["Satisfaction"].mean()

bench=gdpMean/satisMean
ap=lambda a:a*bench

df["Satisfaction"]=df["Satisfaction"].apply(ap)

pl.plot(df["Id"],df["GDP"],label="GDP",marker="o")
pl.plot(df["Id"],df["Satisfaction"],label="Happy",marker="x")
"""

print(df)
pl.plot(df["GDP"],df["Satisfaction"],marker="o")

pl.legend()
pl.show()