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
