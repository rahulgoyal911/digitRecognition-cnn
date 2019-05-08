# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

# Load the classifier
clf = joblib.load("digits_cls.pkl")

# Read the input image 
im = cv2.imread("frame0.jpg")
im = im[10:50,80:95]
# cv2.imshow("aa",im)
# cv2.waitKey()
# Convert to grayscale and apply Gaussian filtering
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# im_gray = cv2.GaussianBlur(im_gray, (5, 5), 1)
im_gray = cv2.bitwise_not(im_gray)
# cv2.imshow("aa",im_gray)
# cv2.waitKey()
# Threshold the image
ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

# Find contours in the image
ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow("aa",im_gray)
# Get rectangles contains each contour
rects = [cv2.boundingRect(ctr) for ctr in ctrs]

# For each rectangular region, calculate HOG features and predict
# the digit using Linear SVM.
for rect in rects:
    # Draw the rectangles
    cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
    # Make the rectangular region around the digit
    leng = int(rect[3] * 40)
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
    cv2.imshow("aa",roi)
    cv2.imwrite("black.jpg",roi)
    cv2.waitKey()
    break

# cv2.imshow("Resulting Image with Rectangular ROIs", im)
# cv2.waitKey()
