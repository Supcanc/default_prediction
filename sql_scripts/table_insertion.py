import mysql.connector
import sys

sys.path.append('../default_prediction/')

from db_connect_args import config

db = mysql.connector.connect(
    **config,
    database='default_prediction',
    allow_local_infile=True
)

cursor = db.cursor()

cursor.execute("""
LOAD DATA LOCAL INFILE 'dataset/prepared_for_insertion.csv' INTO TABLE credit_risk
FIELDS TERMINATED BY ','
IGNORE 1 LINES;
""")

db.commit()

db.close()