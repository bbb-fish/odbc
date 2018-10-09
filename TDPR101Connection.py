#!/usr/bin/env python
"""Quick and easy connection to Aster

"""
import numpy as np
import pandas as pd
import sys, os, pyodbc

def query(sql):
	"""Connects to Aster and returns a Pandas data frame
    
	Arguments:

	A SQL statement in string format 

	"""
	conn = pyodbc.connect('dsn=ConnectR')
	df = pd.read_sql(sql,conn)
	conn.close()
	return df

if __name__ == "__main__":
	query(sys.argv[0])
	#print(query(sys.argv[1]))