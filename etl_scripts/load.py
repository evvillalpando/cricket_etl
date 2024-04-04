import json
import os
import sqlite3

def load():
    print("""
----------------------
--- STARTING LOAD ----
----------------------
        """)

    conn = sqlite3.connect('./cricket_database.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute('DROP TABLE IF EXISTS load_match_data;')
    cursor.execute('''
        CREATE TABLE load_match_data (
            match_id int PRIMARY KEY,
            info blob,
            innings blob
        );''')

    json_files = [file for file in os.listdir('./data/json_files') if file.endswith('.json')]
    print(f'\t-Loading {len(json_files)} files to cricket_database.load_match_data...')
    for json_file in json_files:

        with open(f"./data/json_files/{json_file}", 'r') as file:
            data = json.load(file)

        file_name = json_file.split('.')[0]
        info = json.dumps(data['info']).replace("'", "''")
        innings = json.dumps(data['innings']).replace("'", "''")

        cursor.execute(f"""
            INSERT INTO load_match_data (match_id, info, innings)
            VALUES ({file_name}, '{info}', '{innings}')
            ;""")

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print('\t-Successfully loaded files\n')
