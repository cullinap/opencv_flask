import os
from api import allowed_file
from werkzeug.utils import secure_filename

def handle_file_upload(upload_file, dest_dir, dest_len=None, save=True):
	upload = upload_file
	if upload == None:
		return {"detail": "File not found"}, 404
	if upload.filename == "" and allowed_file(upload.filename):
		return {"detail": "Filename not valid"}, 400
	filename = secure_filename(upload.filename)
	_, ext = os.path.splitext(filename)
	new_filename = filename
	print(dest_dir)
	if dest_len != None:
		new_filename = f"{dest_len}{ext}"
	dest_path = os.path.join(dest_dir, new_filename)
	if save == True:
		upload.save(dest_path)
		return {"saved": True}, 201
	return {"saved": False}, 200

