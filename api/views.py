from flask import send_from_directory, request
from api import app, allowed_file
from werkzeug.utils import secure_filename


@app.route("/")
def home_view():
	return "<h1>Hello World</h1>"

@app.route("/static/uploads/<filename>")
def static_uploads_view(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/api/upload", methods=["POST"])
def api_upload_view():
	if request.method == "POST":
		print(request.files.get("upload_file"))
	return "Hello world"


		# print(request.files.get("file"))  #add .get
	# 	upload = request.files.get("file")
	# 	if upload == None:
	# 		return {"detail": "File not found"}, 404
	# 	if upload.filename == "":
	# 		return {"detail": "Filename not valid"}, 400
	# 	filename = secure_filename(upload.filename)
	# 	dest_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	# 	upload.save(dest_path)

	# return "Hello world"
