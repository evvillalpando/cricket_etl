import sqlite3

class Transform():
    """

    """

    def __init__(self, tables):
        print("""
-------------------------------
--- STARTING TRANSFORMATION ---
-------------------------------
            """)

        self.conn = sqlite3.connect('./cricket_database.db')
        self.cursor = self.conn.cursor()
        self.tables = tables
        self.table_scripts = {
            'matches' : {
                'create_script' : './etl_scripts/sql_scripts/create_matches_table.sql',
                'insert_script' : './etl_scripts/sql_scripts/insert_matches_data.sql'
            },
            'ball_by_ball' : {
                'create_script' : './etl_scripts/sql_scripts/create_ball_by_ball_table.sql',
                'insert_script' : './etl_scripts/sql_scripts/insert_ball_by_ball_data.sql'
            }
        }

    def transform_tables(self):
        for table in self.tables:
            print(f'\t-Create/Recreating table {table}')
            self.execute_sql_file(self.table_scripts[table]['create_script'])
            print(f'\t-Transforming data to cricket_database.{table}')
            self.execute_sql_file(self.table_scripts[table]['insert_script'])
            print(f'\t-cricket_database.{table} ready.\n')

        return True

    def execute_sql_file(self, sql_file):
        with open(sql_file, 'r') as sql_script:
            self.cursor.executescript(sql_script.read())
        self.conn.commit()
        return True

    def close_conn(self):
        self.conn.close()
        return True
