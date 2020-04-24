import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, 'abc.png')

files = {'upload_file': open(filepath, 'rb')}

url = 'http://127.0.0.1:8000/api/upload'

r = requests.post(url, files=files)

print(r.text)