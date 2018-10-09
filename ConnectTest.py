import os
import pyodbc
import pandas as pd

#Setup Database Connection and run query
conn = pyodbc.connect('dsn=ConnectR')
cursor = conn.cursor()
cursor.execute('SELECT * FROM DLABBUAnalytics_Lab.Anomaly_Detection_SuperSet;')
output = cursor.fetchall()

#Delete old csv of data if there is one
try:
    os.remove('C:\\Users\\p2813634\\Desktop\\Work\\Anomaly_Detection\\Data\\test_set2.csv')
except OSError:
    pass

#Convert data pulled from database from list to dataframe
df = pd.DataFrame(output)
#Save Dataframe as csv file -- LATER NEED TO ADD VERSIONING -- Right now it just deletes
df.to_csv('C:\\Users\\p2813634\\Desktop\\Work\\Anomaly_Detection\\Data\\test_set2.csv')
print(df)


#



#df = pd.DataFrame(output, columns = ['MASDIV','STATION','TUNING_EVNT_START_DT','DOW','MOY','TRANSACTIONS'])
#print(df)
