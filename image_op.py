import cv2
import imutils
import time
import os.path
from human_detector import detector

imgs = []
path = "C:/Users/marty/Desktop/Projekt/pics"
valid_images = [".jpg", ".png"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(cv2.imread(path + "/" + f))

for img_path in imgs:
    start_time = time.time()
    img = detector(imutils.resize(img_path, width=700))
    print("--- %s seconds ---" % (time.time() - start_time))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
