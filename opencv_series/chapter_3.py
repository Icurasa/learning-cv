import cv2
import numpy as np

path = "../images/dog.jpeg"
img = cv2.imread(path)

kernel = np.ones((5, 5), np.float32) / 25
img_f = cv2.filter2D(img, -1, kernel)

cv2.imshow('img', img)
cv2.imshow('img2', img_f)

cv2.waitKey(0)
