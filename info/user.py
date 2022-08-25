import imp
import pandas as pd
import numpy as np
import json
import sys
sys.path.append('info')
import mongo

class User:
    def __init__(self):
        #self.userData = pd.read_csv('./data/event.csv')
        self.mongoObj = mongo.MongoConnect('events')
        self.userData = self.mongoObj.data
    
    def ExpPerUser(self):
        buffer = self.userData.groupby('userID').sum()['expenses']
        y = buffer.tolist()
        x = self.userData.userID.unique().tolist()
        # convert all elements in x to str
        x = [str(i) for i in x] 
        data = {'x': x, 'y': y}
        return json.dumps(data)
    
    def ReachPerUser(self):
        buffer = self.userData.groupby('userID').sum()['peopleReached']
        y = buffer.to_list()
        x = self.userData.userID.unique().tolist()
        x = [str(i) for i in x] 
        data = {'x': x, 'y': y}
        return json.dumps(data)

    def CountVsType(self):
        buffer = self.userData.groupby('type').count()['userID']
        y = buffer.to_list()
        x = self.userData.type.unique().tolist()
        x = [str(i) for i in x] 
        data = {'x': x, 'y': y}
        return json.dumps(data)
    
    def reportStatus(self):
        buffer = self.userData.groupby('status').count()['userID']
        y = buffer.to_list()
        x = self.userData.status.unique().tolist()
        x = [str(i) for i in x]
        data = {'x': x, 'y': y}
        return json.dumps(data)
