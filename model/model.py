import pyod.models.xgbod as XGBOD

class Model:
    def __init__(self, X, y=None, model=None):
        if y is None:
            self.model = self.train(X)
        else:
            self.model = self.train(X, y)
        self.prediction = self.predict(X) # Predict the model


    def train(self, X, y=None, model=None):

        if model is 'XGBOD':
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
        return self.model.predict(X) # Predict the target values
