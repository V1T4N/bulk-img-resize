import cv2
import glob

files = glob.glob("./img/*")

w = int(input("width>>"))

for fname in files:
    print(fname)
    img = cv2.imread(fname)
    height, width = img.shape[:2]
    img2 = cv2.resize(img,(w,int(height*(w/width))))
    cv2.imwrite("./r/r_" + fname[6:] , img2)