import pandas as pd
from matplotlib import pyplot as pl

df=pd.read_csv(r"/home/ml_enigma/Documents/Coding/ML/prac/data1.csv")

print(df["humidity(%)"])
print(df.iloc[2:4])
#print(df.iloc[2:5][df["wind(KM/H)"]>5])
df["mod_hum"]=df["humidity(%)"].apply(lambda a:a*1.5)
print(df["mod_hum"])

""" 
t=df["ID"].str.strip("(")
print(t)
"""

pl.plot(df["ID"],df["humidity(%)"],linestyle='-',label='Humidity',marker='*',color='red')
pl.plot(df["ID"],df["degrees(C)"], linestyle='-.' ,label='Degrees',marker='o',color='blue')
pl.fill_between(df["ID"],df["humidity(%)"],df["degrees(C)"],color='grey',alpha=0.3)
pl.plot(df["ID"],df["wind(KM/H)"],label="wind",linestyle=":",marker="X",color="orange")
pl.fill_between(df["ID"],df["degrees(C)"],df["wind(KM/H)"],color="yellow",alpha=0.3)
pl.xlabel("ID")
pl.ylabel("Humidity (%),wind(KM/H),degrees(C)")
pl.legend()
pl.show()

