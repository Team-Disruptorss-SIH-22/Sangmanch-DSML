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
    
    def monthlyData(self):
        data = self.userData.loc[0:280]
        data['date'] = pd.to_datetime(data['date'],unit='ms')
        data['date'] = data['date'].dt.strftime('%Y-%m-%d')
        data['date'] = [date.split('-') for date in data['date']]
        month = [date[1] for date in data['date']]
        data['month'] = month[:]
        buffer = data.groupby('month').count()['userID']
        y = buffer.to_list()
        x = data.month.unique().tolist()
        x = [(str(i)) for i in x]
        # sort x
        x.sort()
        data = {'x': x, 'y': y}
        return json.dumps(data)


'''if __name__ == '__main__':
    user = User()
    print(user.monthlyData())'''