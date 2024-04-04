import requests
import os
import zipfile

class Extract():

    def __init__(self):
        self.zip_files_path = "./data/zip_files"
        self.json_files_path = "./data/json_files"
        print("""
----------------------
-- STARTING EXTRACT --
----------------------
            """)

    def download_zip(self, url):

        print('Beginning download of zip file...')
        # Use requests to get the zip file from url
        response = requests.get(url)

        if response.status_code == 200:
            # Get file name of downloaded zip, concat to path for zip files
            response_file_name = response.url.split('/')[-1]
            zip_path = f"{self.zip_files_path}/{response_file_name}"

            # Write zip file
            with open(zip_path, 'wb') as file:
                file.write(response.content)

            print(f"\t-Download of zip file completed. Path to zip: {zip_path}\n")
            # Return the path of the downloaded zip file
            return zip_path

        else:
            print(f"\t-Unsuccessful request on url '{url}'. Reponse status code {response.status_code}")

    def extract_zip(self, zip_path):
        # Extract zip file contents
        print('Beginning extraction of zip file...')
        with zipfile.ZipFile(zip_path, 'r') as zip_to_extract:
            print(f"\t-Extracting {len(zip_to_extract.namelist())} files to {self.json_files_path}")
            zip_to_extract.extractall(self.json_files_path)
        print("\t-Zip file successfuly extracted\n")
