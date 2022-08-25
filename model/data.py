import sys
sys.path.extend(['info','model'])
import mongo, user, test, finance
import os
import pandas as pd

class Data():
    def __init__(self, table):
        self.mongoOBJ = mongo.MongoConnect(table)
        self.dataTable = self.mongoOBJ.load_table(table)
        print(self.dataTable.columns)
        self.dataTable['_id'] = self.dataTable['_id'].astype(str)
        self.expenses = self.dataTable.groupby('userID').sum()['expenses']
        self.peopleReached = self.dataTable.groupby('userID').sum()['peopleReached']
        self.eventType = self.dataTable.groupby('userID').count()['type']

        self.y = self.dataTable.groupby('userID').count()['status'] # focus on -1 and 1

if __name__ == "__main__":
    dataOBJ = Data('events')
    print(dataOBJ.y)

