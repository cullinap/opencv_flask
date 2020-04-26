import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)
img_path = os.path.join(BASE_DIR, 'espn.png')

frame = cv2.imread(img_path)
og_frame = cv2.imread(img_path)
gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier(cascade_path)
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(faces)
for i, (x, y, w, h) in enumerate(faces):
	roi_color = frame[y:y+h, x:x+w]
	path = os.path.join(OUTPUT_DIR, f"{i}.jpg")
	color = (255, 0, 0) #BGR
	cv2.rectangle(og_frame, (x, y), (x+w, y+h), color, 2)
	cv2.imwrite(path, roi_color)
cv2.imwrite(os.path.join(OUTPUT_DIR, 'espn.png'), og_frame)
# cv2.imshow("frame", frame)
# cv2.imshow("gray", gray)
cv2.waitKey(0) # press w to quit
cv2.destroyAllWindows()

