import sys
sys.path.extend(['info','model'])
import mongo, user, test, finance
import os
import pandas as pd

class Data():
    def __init__(self, table):
        # Load the data from the database
        self.mongoOBJ = mongo.MongoConnect(table)
        self.dataTable = self.mongoOBJ.load_table(table)

        # convert id to string
        self.dataTable['_id'] = self.dataTable['_id'].astype(str)

        # get data with status as 'approved' or 'rejected' by finance manager
        self.dataTable = self.dataTable[(self.dataTable['status'] == -1) | (self.dataTable['status'] == 1)]

        # training data: x
        self.expenses = [x for x in self.dataTable['expenses']]
        self.peopleReached = [x for x in self.dataTable['peopleReached']]
        self.eventType = [x for x in self.dataTable['type']] 

        # testing data: y
        self.status = [x for x in self.dataTable['status']]

        

if __name__ == "__main__":
    dataOBJ = Data('events')
    print(dataOBJ.status)
