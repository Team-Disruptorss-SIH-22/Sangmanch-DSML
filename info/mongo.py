from distutils.log import ERROR
import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
#check
class MongoConnect():
    def __init__(self, table):
        self.data = self.load_table(table)       
    
    def load_secrets(self):
        load_dotenv()
        return os.getenv('URI_SECRET')

    def load_table(self, table):  
        client = MongoClient()
        #client = MongoClient(self.load_secrets())
        client = MongoClient('mongodb+srv://admin:pTvYVDmoNWcEUHy9@cluster0.wcg0e.mongodb.net/?retryWrites=true&w=majority')
        db = client['test']
        if table == 'events':
            events = db.events
            events = pd.DataFrame(list(events.find()))
            return events
        
        elif table == 'users':
            users = db.users
            users = pd.DataFrame(list(users.find()))
            return users
        
        elif table == 'financereports':
            financereports = db.financereports
            financereports = pd.DataFrame(list(financereports.find()))
            return financereports
        
        elif table == 'generalassemblyreports':
            generalassemblyreports = db.generalassemblyreports
            generalassemblyreports = pd.DataFrame(list(generalassemblyreports.find()))
            return generalassemblyreports
        
        elif table == 'governingbodyreports':
            governingbodyreports = db.governingbodyreports
            governingbodyreports = pd.DataFrame(list(governingbodyreports.find()))
            return governingbodyreports
        
        else:
            raise Exception('Table not found')

