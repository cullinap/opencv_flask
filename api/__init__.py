import os
from flask import Flask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "storage", "upload")
RESULTS_DIR = os.path.join(BASE_DIR, "storage", "results")
OUPUT_DIR = os.path.join(BASE_DIR, "storage", "output")

for d in [UPLOAD_DIR, RESULTS_DIR, OUPUT_DIR]:
	os.makedirs(d, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def home_view():
	return "<h1>Hello World</h1>"