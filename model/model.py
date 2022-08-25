import pyod.models.xgbod as XGBOD

class Model:
    def __init__(self, X, y=None):
        if y is None:
            self.model = self.train(X)
        else:
            self.model = self.train(X, y)
        self.prediction = self.predict(X) # Predict the model


    def train(self, X, y):
        from pyod.models.ecod import ECOD
        clf = XGBOD() # Using default settings
        clf.fit(X, y) # Train the model
        return clf
    
    def predict(self, X):
        return self.model.predict(X) # Predict the target values
