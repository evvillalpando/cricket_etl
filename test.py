import os
import json

def get_distinct_json_keys(folder_path):
    distinct_keys = set()

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            # Open and load JSON file
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                # Collect distinct keys
                for key in json_data['info'].keys():
                    distinct_keys.add(key)
                    if isinstance(json_data['info'][key], dict):
                        for key2 in json_data['info'][key].keys():
                            distinct_keys.add(key + '->' + key2)

    return distinct_keys

# Example usage:
folder_path = './data/json_files'
distinct_keys = get_distinct_json_keys(folder_path)
print("Distinct JSON keys:", distinct_keys)
