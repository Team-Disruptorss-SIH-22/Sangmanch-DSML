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
        self.eventTypeENUM = []

        for i in self.eventType:
            # "scholarship", "festival", "seminar", "languageFest", "culturalFest", "exhibition"
            if i == 'scholarship':
                self.eventTypeENUM.append(2)
            elif i == 'festival':
                self.eventTypeENUM.append(1.2)
            elif i == 'seminar':
                self.eventTypeENUM.append(1.1)
            elif i == 'languageFest':
                self.eventTypeENUM.append(1.1)
            elif i == 'culturalFest':
                self.eventTypeENUM.append(1.2)
            elif i == 'exhibition':
                self.eventTypeENUM.append(1.1)
            else:
                self.eventTypeENUM.append(1)
        
        # formula = (expenses/peopleReached)^eventType
        self.x = [(x/y)**z for x,y,z in zip(self.expenses, self.peopleReached, self.eventTypeENUM)]
        
        # testing data: y
        self.y = [x for x in self.dataTable['status']]

        

if __name__ == "__main__":
    dataOBJ = Data('events')
    print(dataOBJ.x)
    #print(dataOBJ.status)
