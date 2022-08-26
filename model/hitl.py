import sys
sys.path.extend(['info','model'])
import sys
import data, model
import pandas as pd
import numpy as np

class HITL():
    def __init__(self, val, model_='XGBOD', table='events'):
        self.modelChoice = model_
        self.table = table
        self.val = val
        #print(self.val)
        # Load the data
        self.dataOBJ = data.Data(self.table)
        self.x = self.dataOBJ.x
        self.x = np.array(self.x).reshape(-1,1)
        #self.x = np.round(self.x, 3)
        self.y = self.dataOBJ.y
        # if y is -1 change to 0
        self.y = [0 if x == -1 else x for x in self.y]
        #print(self.x)
        #exit()

        # Train the model
        self.modelOBJ = model.Model(X=self.x, y=self.y, model=self.modelChoice, val=self.val)
        self.prediction = self.modelOBJ.prediction


if __name__ == "__main__":
    val = np.array([4.0]).reshape(-1,1)
    hitlOBJ = HITL(val, model_='XGBOD')
    print(hitlOBJ.prediction)


        
