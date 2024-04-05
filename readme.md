# Reproducing cricket_etl
1. Ensure sqlite version >= 3.38.0 is installed on your machine. SQL code for parsing jsons may error our if using a lesser version. https://www.sqlite.org/download.html
2. Open CLI tool and change working directory to wherever this repo is cloned.
2. Create a venv using requirements:
  2a. In terminal or conda prompt, type `python -m venv myvenv`
  2b. Activate the venv. Use `myvenv\Scripts\activate` for Windows, `source myvenv/bin/activate`
  2c. `pip install -r requirements.txt`
3. Run python main.py in CLI. Its arguments include extract, transform, load, query. For example,
`python main.py extract transform load query` will run the entire cricket pipeline.
#### extract
- downloads zip file from cricksheet and unzips json files.
#### load
- loads raw json files into load_match_data table in cricket_database.
#### transform
- uses sql to parse out the json to produce ball-by-ball data and match results.
#### query
- provides the answers to question 2.
