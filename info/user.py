import pandas as pd
import numpy as np
import json

class Finance:
    def __init__(self):
        self.userData = pd.read_csv('./data/event.csv')
        self.userData['expense'] = self.userData['expense'].str[1:].astype('float32')
        self.userData['budget'] = self.userData['budget'].str[1:].astype('float32')
    
    def ExpPerUser(self):
        buffer = self.userData.groupby('user_id').sum()['expense']
        y = buffer.to_list()
        x = self.userData.user_id.unique().tolist()
        data = {'x': x, 'y': y}
        return json.dumps(data)
    
    def ReachPerUser(self):
        buffer = self.userData.groupby('user_id').sum()['reach']
        y = buffer.to_list()
        x = self.userData.user_id.unique().tolist()
        data = {'x': x, 'y': y}
        return json.dumps(data)
    
