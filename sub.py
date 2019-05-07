# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np


# Read the input image 
im = cv2.imread("frame0.jpg")
im1=cv2. imread("frame1.jpg")
im3 = cv2.subtract(im,im1)
cv2.imshow("aa",im3)
cv2.waitKey()
# im[int(2):int(121), int(13):int(149)]
