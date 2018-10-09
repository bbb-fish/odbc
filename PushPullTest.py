
'''
Written by Bobby Fisher October 1st, 2018
REFERENCE
https://tomaztsql.wordpkress.com/2018/07/15/using-python-pandas-dataframe-to-read-and-insert-data-to-microsoft-sql-server/
'''

import pandas as pd
import pyodbc
from datetime import datetime

#READ IN CSV TEST DATA
df = pd.read_csv('C:\\Users\\p2813634\\Desktop\\Work\\Anomaly_Detection\\Data\\trx_20180924.csv')
print('CSV LOADED')

#ADJUST DATE FORMAT
df['TUNING_EVNT_START_DT'] = pd.to_datetime(df.TUNING_EVNT_START_DT)
df['TUNING_EVNT_START_DT'] = df['TUNING_EVNT_START_DT'].dt.strftime('%Y-%m-%d')
print('DATE FORMAT CHANGED')
print(df.shape)
print(df.head(10))

#PUSH TO DATABASE
conn = pyodbc.connect('dsn=ConnectR')
cursor = conn.cursor()

# Database table has columns...
# PK | TRXYPE | MASDIV | STATION | TUNING_EVNT_START_DT | DOW | MOY | TRANSACTIONS | ANOMALY_FLAG
# PK is autoincrementing, TRXTYPE needs to be specified on insert command, and ANOMALY_FLAG defaults to 1 for yes

for index, row in df.iterrows():
        cursor.execute("INSERT INTO DLABBUAnalytics_Lab.Anomaly_Detection_SuperSet(MASDIV,TRXTYPE,STATION,TUNING_EVNT_START_DT,DOW,MOY,TRANSACTIONS)VALUES(?,?,?,?,?,?,?)", row['MASDIV'],'non_chtr',row['STATION'],row['TUNING_EVNT_START_DT'],row['DOW'],row['MOY'],row['TRANSACTIONS'])
        conn.commit()
        print('RECORD ENTERED')

print('DF SUCCESSFULLY WRITTEN TO DB')

#PULL FROM DATABASE
sql_conn = pyodbc.connect('dsn=ConnectR')
query = 'SELECT * FROM DLABBUAnalytics_Lab.Anomaly_Detection_SuperSet;'
df = pd.read_sql(query, sql_conn)
print(df.head(10))
