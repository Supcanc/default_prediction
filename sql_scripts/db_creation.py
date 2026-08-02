import mysql.connector
import sys

sys.path.append('../default_prediction/')

from db_connect_args import config

db = mysql.connector.connect(**config)

cursor = db.cursor()

cursor.execute("CREATE DATABASE default_prediction;")

db.close()