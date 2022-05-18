import csv
import json
import psycopg2


json_path = r'C:\Briefcase_2021\Learning_2021\Python\Python\Scenarios\Reading_Write_JSON_Files\database_env.json'
with open(json_path) as json_data:
    env_data = json.load(json_data)

v_host = env_data['host']
v_database = env_data['database']
v_port = env_data['port']
v_username = env_data['user']
v_password = env_data['password']


def load_big_table(v_file_name,v_table_name)
    try:
        print('Connecting to the database')
        conn = psycopg2.connect(dbname=v_database, host=v_host, port=v_port,\
        user = v_username, password=v_password)
        cur = conn.cursor()
        print("Connection successfully to Database")
        f = open(v_file_path, "r")
        cur.copy_expert("copy {} from CSV HEADER QUOTE '\"'".format(v_table_name), f)
        cur.execute("commit;")
        print("Loaded data into {}".format(v_table_name))
        conn.close()
        print("Database connection closed.")
    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


load_big_table(v_file_name,v_table_name)

=====================================================================
    Second Method Using cur.execute for each row
=====================================================================

import csv
import json
import psycopg2

json_path = r'C:\Briefcase_2021\Learning_2021\Python\Python\Scenarios\Reading_Write_JSON_Files\database_env.json'
with open(json_path) as json_data:
    env_data = json.load(json_data)

v_host = env_data['host']
v_database = env_data['database']
v_port = env_data['port']
v_username = env_data['user']
v_password = env_data['password']

try:
    print('Connecting to the database')
    conn = psycopg2.connect(dbname=v_database, host=v_host, port=v_port,\
    user=v_username, password=v_password)
    cur = conn.cursor()
    print("Connection successfully to Database")
except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)",
        row
    )
conn.commit()
conn.close()

=====================================================================
## Using Pandas and Chunksize
=====================================================================

import csv
import json
import psycopg2
import pandas as pd


json_path = r'C:\Briefcase_2021\Learning_2021\Python\Python\Scenarios\Reading_Write_JSON_Files\database_env.json'
with open(json_path) as json_data:
    env_data = json.load(json_data)

v_host = env_data['host']
v_database = env_data['database']
v_port = env_data['port']
v_username = env_data['user']
v_password = env_data['password']


try:
    print('Connecting to the database')
    conn = psycopg2.connect(dbname=v_database, host=v_host, port=v_port,\
    user=v_username, password=v_password)
    cur = conn.cursor()
    print("Connection successfully to Database")
except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


# Open csv file as stream and write to SQL, appending as you go:
for chunk in pd.read_csv('filename.csv', chunksize = 1000):
    chunk.to_sql(name = 'huge_table',
                 con = conn,
                 if_exists = 'append')

conn.close()                 