import pandas as pd
from matplotlib import pyplot as pl

df=pd.read_csv(r"/home/ml_enigma/Documents/Coding/ML/prac/data1.csv")

class Plots:
    def __init__(self):
        self.data=df 
        
    def graph(self):
        pl.plot(self.data["ID"],self.data["degrees(C)"],color="blue",label="Temp")
        pl.plot(self.data["ID"],self.data["humidity(%)"],color="red",label="Humid")
        pl.plot(self.data["ID"],self.data["wind(KM/H)"],label="wind",color="orange")
        pl.legend()
        pl.show()
   
class ch_Plots(Plots):
    def __init__(self):
        super().__init__()
        self.days=self.data["ID"]
        
    def viewData(self):
        print("The Data:")
        print(self.data)
        
    def check_rain(self):
        while self.data["is_rain"]==True:
            if self.data["is_rain"]==True:
                print(f"There is rain on day {self.data['ID']}")
            else:
                print(f"There is no rain on day {self.data['ID']}")
        
        
ar=Plots()
br=ch_Plots()

br.viewData()