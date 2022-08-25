import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

def load_secrets():
    load_dotenv()
    return os.getenv('URI_SECRET')

def main():
    client = MongoClient()
    #point the client at mongo URI
    client = MongoClient(load_secrets())
    #select database
    db = client['test']
    #select the collection within the database
    test = db.events
    #convert entire collection to Pandas dataframe
    test = pd.DataFrame(list(test.find()))
    print(test.head())

if __name__ == '__main__':
    main()