import sys
import os
from etl_scripts import extract, transform, load

args = sys.argv[1:]

json_file_dir = './data/json_files'
if not os.path.exists(json_file_dir):
    os.makedirs(json_file_dir)
    print("Created directory for json files")

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
    transformer = transform.Transform(tables=['matches'])
    transformer.transform_tables()
    transformer.close_conn()
