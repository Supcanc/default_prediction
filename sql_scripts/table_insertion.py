import mysql.connector
import sys

sys.path.append('../default_prediction/')

from db_connect_args import config

db = mysql.connector.connect(
    **config,
    database='default_prediction'
)

cursor = db.cursor()

cursor.execute("""

""")

db.commit()

db.close()