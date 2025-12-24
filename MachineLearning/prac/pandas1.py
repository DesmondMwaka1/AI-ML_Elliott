from matplotlib import pyplot as pt 
import pandas as pd

df=pd.read_csv(r"prac/advSales.csv")
print(df["adv"])
print(df.iloc[1:4])
print(df.iloc[4,2])