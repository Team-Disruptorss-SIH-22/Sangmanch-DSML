import pandas as pd
import numpy as np
import json
import sys
sys.path.append('info')
import mongo

mongoObj = mongo.MongoConnect('events')
userData = mongoObj.data
buffer = userData.groupby('userID').sum()['expenses']
y = buffer.tolist()
x = userData.userID.unique().tolist()
data = {'x': x, 'y': y}


#print(json.dumps(data, indent=4))