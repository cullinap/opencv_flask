import os
import cv2
from api import OUTPUT_DIR

def get_cascade(cascade_xml='haarcascade_frontalface_default.xml'):
	cascade_path = os.path.join(cv2.data.haarcascades, cascade_xml)
	cascade = cv2.CascadeClassifier(cascade_path)
	return cascade

def extract(img_path):
	cascade  = get_cascade()
	filename, _ = os.path.splitext(os.path.basename(img_path))
	final_output_dir = os.path.join(OUTPUT_DIR, f"{filename}")
	os.makedirs(final_output_dir, exist_ok=True)
	frame = cv2.imread(img_path)
	og_frame = cv2.imread(img_path)
	gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
	for i, (x, y, w, h) in enumerate(faces):
		roi_color = frame[y:y+h, x:x+w]
		path = os.path.join(final_output_dir, f"{i}.jpg")
		color = (255, 0, 0) #BGR
		cv2.rectangle(og_frame, (x, y), (x+w, y+h), color, 2)
		cv2.imwrite(path, roi_color)
	cv2.imwrite(os.path.join(final_output_dir, 'espn.png'), og_frame)
	return final_output_dir


# img_path = os.path.join(BASE_DIR, 'espn.png')
# frame = cv2.imread(img_path)
# og_frame = cv2.imread(img_path)
# gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# #print(faces)
# for i, (x, y, w, h) in enumerate(faces):
# 	roi_color = frame[y:y+h, x:x+w]
# 	path = os.path.join(OUTPUT_DIR, f"{i}.jpg")
# 	color = (255, 0, 0) #BGR
# 	cv2.rectangle(og_frame, (x, y), (x+w, y+h), color, 2)
# 	cv2.imwrite(path, roi_color)
# cv2.imwrite(os.path.join(OUTPUT_DIR, 'espn.png'), og_frame)
# # cv2.imshow("frame", frame)
# # cv2.imshow("gray", gray)
# cv2.waitKey(0) # press w to quit
# cv2.destroyAllWindows()

