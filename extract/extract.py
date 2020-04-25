import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, 'espn.png')

frame = cv2.imread(img_path)
gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.imshow("frame", frame)
cv2.imshow("gray", gray)
cv2.waitKey(0) # press w to quit
cv2.destroyAllWindowns()