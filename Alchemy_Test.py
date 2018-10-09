import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

#SQL ALCHEMY STUFF
user = 'E813634'
pasw = 'DQX1duds!'
host = '142.136.184.160'

# connect
td_engine = create_engine('teradata://'+ user +':' + pasw + '@'+ host + '/' + '?authentication=LDAP')
print(td_engine)

# execute sql
result = td_engine.execute('SELECT * FROM DLABBUAnalytics_Lab.Anomaly_Detection_SuperSet;')
#print(result)
