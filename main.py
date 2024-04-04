import sys
import sqlite3
import os
import pandas as pd
from etl_scripts import extract, transform, load

args = sys.argv[1:]

if 'extract' in args:
    # Begin extraction
    extractor = extract.Extract()
    ## Download zip file and get path to downloaded zip
    zip_path = extractor.download_zip("https://cricsheet.org/downloads/odis_json.zip")
    ## Extract contents of zip file
    extractor.extract_zip(zip_path)

if 'load' in args:
    load.load()

if 'transform' in args:
    transformer = transform.Transform(tables=['matches', 'ball_by_ball', 'players'])
    transformer.transform_tables()
    transformer.close_conn()

if 'query' in args:
    conn = sqlite3.connect('./cricket_database.db')
    cursor = conn.cursor()

    # Loop through queries to answer question 2
    print("""
-------------------------------------
--Query results for questions 2a-2c--
-------------------------------------
        """)
    for file in ['./question_2_queries/q2a.sql', './question_2_queries/q2b.sql', './question_2_queries/q2c.sql']:
        with open(file, 'r') as f:
             sql_script = f.read()
        df = pd.read_sql_query(sql_script, conn)
        print(df, '\n')
