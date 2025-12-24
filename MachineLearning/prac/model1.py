import numpy as np

x=['A','B','A','A','B']
y=[1,1,0,1,1]

class model1:
    def __init__(self):
        self.mode={}
        
    def fit(self):
        counter = {}
        for index, label in enumerate(x):
            if label not in counter:
                counter[label] = [0, 0]
            counter[label][y[index]] += 1
            self.mode[label] = np.argmax(counter[label])
        return self.mode
                
    def predict(self):
        res = []
        for label in x:
            if label in self.mode:
                res.append(self.mode[label])
            else:
                res.append(None)
        return res

a=model1()
print(a.fit())
print(a.predict())