# import pandas as pd
# import json
# import sqlite3
#
#
# json_file_path = '/Users/villalpando/Documents/cricket_etl/data/json_files/64814.json'
#
# # Load the JSON file into a Python dictionary
# with open(json_file_path, 'r') as file:
#     data = json.load(file)['info']
#
# df = pd.json_normalize(data)
#
# df['match_id'] = df.apply(lambda x : f"{x['dates'][0].replace('-','')}_{'_'.join(x['teams'])}".lower(), axis=1)
# df['game_start_date'] = df['dates'][0]
# # print(df[['match_id', 'game_start_date']])
