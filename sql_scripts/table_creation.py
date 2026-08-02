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
CREATE TABLE credit_risk(
    client_ID CHAR(10) PRIMARY KEY,
    person_age TINYINT UNSIGNED,
    person_income MEDIUMINT,
    person_home_ownership VARCHAR(100),
    person_emp_length TINYINT,
    loan_intent VARCHAR(20),
    loan_grade CHAR(1),
    loan_amnt SMALLINT UNSIGNED,
    loan_int_rate DECIMAL(4, 2),
    loan_status TINYINT UNSIGNED,
    loan_percent_income DECIMAL(3, 2),
    cb_person_default_on_file BOOLEAN,
    cb_person_cred_hist_length TINYINT UNSIGNED,
    gender VARCHAR(6),
    marital_status VARCHAR(10),
    education_level VARCHAR(15),
    country VARCHAR(10),
    state VARCHAR(100),
    city VARCHAR(100),
    city_latitude DECIMAL(10, 4),
    city_longitude DECIMAL(10, 4),
    employment_type VARCHAR(15),
    loan_term_months TINYINT UNSIGNED,
    loan_to_income_ratio FLOAT UNSIGNED,
    other_debt FLOAT UNSIGNED,
    debt_to_income_ratio FLOAT UNSIGNED,
    open_accounts TINYINT UNSIGNED,
    credit_utilization_ratio FLOAT UNSIGNED,
    past_delinquencies TINYINT UNSIGNED
);
""")

db.close()