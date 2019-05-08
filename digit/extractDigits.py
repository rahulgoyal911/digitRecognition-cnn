# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

clf = joblib.load("digits_cls.pkl")
im = cv2.imread("frame0.jpg")
i=0

def function(im,a,b,c,d):
    global i
    # Read the input image 
    im = cv2.imread("frame0.jpg")
    im = im[a:b,c:d]
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
        # cv2.imshow("aa",roi)
        i = i+1
        name = 'images/'
        name += str(i)
        name+='.jpg'
        cv2.imwrite(name,roi)
        # cv2.waitKey()
        break

# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
        success=0
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        function(image,10,50,80,96)
        function(image,20,50,94,106)
        function(image,20,50,106,122)
        function(image,20,50,120,135)

        function(image,50,70,94,106)
        function(image,50,70,106,122)
        function(image,50,70,120,135)

        function(image,70,92,80,96)
        function(image,70,92,94,106)
        function(image,70,92,106,122)
        function(image,70,92,120,135)

        function(image,97,116,80,96)
        function(image,97,116,94,106)
        function(image,97,116,106,122)
        function(image,97,116,120,135)
        # Saves the frames with frame-count 
        # cv2.imwrite("frame%d.jpg" % count, image) 
  
        count += 60
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture("video.VOB") 