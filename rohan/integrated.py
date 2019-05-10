import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np
import io
import os
from google.cloud import vision
from google.cloud.vision import types
from PIL import ImageFilter, Image
import time


iii = 0
i=0

def show(im):
    cv2.imshow("aa",im)
    cv2.waitKey()
def getData(im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,im13,im14):
    show(im1)
    show(im2)
    show(im3)
    show(im4)
    show(im5)
    show(im6)
    show(im7)
    show(im8)
    show(im9)
    show(im10)
    show(im11)
    show(im12)
    show(im13)
    show(im14)

def cropImages(image):
    global iii
    im1 = image[0:28,28:41]
    im2 = image[0:28,41:54]
    im3 = image[0:28,54:68]
    im4 = image[0:28,68:82]
    im5 = image[0:28,82:96]
    im6 = image[0:28,96:110]
    im7 = image[0:28,110:123]
    im8 = image[0:28,166:181]
    im9 = image[0:28,182:193]
    im10 = image[0:28,193:208]
    im11 = image[0:28,208:221]
    im12 = image[0:28,221:237]
    im13 = image[0:28,237:251]
    im14 = image[0:28,250:267]

    getData(im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,im13,im14)

def mainFun():
    cap = cv2.VideoCapture("videos/VTS_15_1.VOB")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    currentFrame = 0
    path_frame ="images/"
    while(currentFrame < length): # making frames from video
        ret, frame = cap.read()
        name = str(currentFrame) + '.jpg'
        print ('Creating frame : ' + name)
        im = frame[0:20,0:290]   # cropping frame
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # converting rgb to gray
        im_gray = cv2.bitwise_not(im_gray)
        im_bw = cv2.threshold(im_gray,160,255,cv2.THRESH_TRUNC)[1] # further image preprocessing
        temp = im_bw
        # cv2.imwrite(path_frame+name, im_bw)
        cropImages(im_bw)
        break
        # currentFrame+=1

    cap.release()
    cv2.destroyAllWindows()



mainFun()