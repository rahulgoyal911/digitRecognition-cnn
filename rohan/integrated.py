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
import csv

def show(im):
    cv2.imshow("aa",im)
    cv2.waitKey()

def recognise(image):
    return 1
def getData(im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,im13,im14):
    # show(im1)
    # show(im2)
    # show(im3)
    # show(im4)
    # show(im5)
    # show(im6)
    # show(im7)
    # show(im8)
    # show(im9)
    # show(im10)
    # show(im11)
    # show(im12)
    # show(im13)
    # show(im14)
    a = str(recognise(im1))
    b = str(recognise(im2))
    c = str(recognise(im3))
    d = str(recognise(im4))
    e = str(recognise(im5))
    f = str(recognise(im6))
    g = str(recognise(im7))
    h = str(recognise(im8))
    i = str(recognise(im9))
    j = str(recognise(im10))
    k = str(recognise(im11))
    l = str(recognise(im12))
    m = str(recognise(im13))
    n = str(recognise(im14))

    e_val = a+b+c+d+e+f+g
    n_val = h+i+j+k+l+m+n
    with open('data.csv', 'w') as csvFile:
        d = ['E','N']
        writer = csv.writer(csvFile)
        writer.writerow(d)
        # print("empty csv file created")
    csvFile.close()
    data_row = [e_val,n_val]
    last = []
    with open('data.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
                last = row
    f.close()
    if(data_row != last):
        with open('data.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data_row)
        csvFile.close()


def cropImages(image):
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
    print(length)
    while(currentFrame < length-2): # making frames from video
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
        # break
        currentFrame+=1

    cap.release()
    cv2.destroyAllWindows()
    print("done")



mainFun()