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
        #self.userData['expenses'] = self.userData['expenses']
        #self.userData['budget'] = self.userData['budget']
    
    def ExpPerUser(self):
        buffer = self.userData.groupby('userID').sum()['expenses']
        y = buffer.tolist()
        x = self.userData.userID.unique().tolist()
        data = {'x': x, 'y': y}
        #return json.dumps(data)
        return data
    
    def ReachPerUser(self):
        buffer = self.userData.groupby('userID').sum()['peopleReached']
        y = buffer.to_list()
        x = self.userData.userID.unique().tolist()
        data = {'x': x, 'y': y}
        #return json.dumps(data)
        return data
    
