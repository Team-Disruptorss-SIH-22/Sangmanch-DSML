import pyod.models.xgbod as XGBOD
import numpy as np

class Model:
    def __init__(self, X, val, y=None,  model='XGBOD', mode='train'):
        print(val)
        self.model = self.train(X, y, model)
        self.prediction = self.predict(val) 


    def train(self, X, y=None, model=None):
        if model == 'XGBOD':
            model = XGBOD.XGBOD(max_depth=3, learning_rate=0.1, n_estimators=100, verbose=True)
            if y == None:
                model.fit(X)
            else:
                model.fit(X, y)
            return model

        elif model == 'LogReg':
            from sklearn.linear_model import LogisticRegression
            model = LogisticRegression()
            if y == None:
                raise Exception('Logistic Regression requires y')
            else:
                model.fit(X, y)
            return model
    
    def predict(self, X):
        X = np.array(X).reshape(-1,1)
        return self.model.predict(X) # Predict the target values
