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

i=0
cap = cv2.VideoCapture("vid.VOB")

def function(im,a,b,c,d):
    global i
    # Read the input image 
    print("called")
    im = im[a:b,c:d]
    i=i+1
    name = "images/"
    name += str(i)
    name+=".jpg"
    cv2.imwrite(name,im)
    
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
currentFrame = 0
path_frame ="images/"
while(currentFrame < length): # making frames from video
    ret, frame = cap.read()
    name = str(currentFrame) + '.jpg'
    # name = str(i)+'.jpg'
    print ('Creating frame : ' + name)
    im = frame[0:20,0:290]   # cropping frame
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # converting rgb to gray
    im_gray = cv2.bitwise_not(im_gray)
    im_bw = cv2.threshold(im_gray,160,255,cv2.THRESH_TRUNC)[1] # further image preprocessing
    temp = im_bw
    cv2.imwrite(path_frame+name, im_bw)
    currentFrame+=1
    # im_bw = i/m_bw[20:30,30:80]
    # print(im_bw)
    # function(im_bw,0,28,10,28)
    # function(im_bw,0,28,28,41)
    # function(im_bw,0,28,41,54)
    # function(im_bw,0,28,54,68)
    # function(im_bw,0,28,68,82)
    # function(im_bw,0,28,82,96)
    # function(im_bw,0,28,96,110)
    # function(im_bw,0,28,110,123)
    


    # cv2.imwrite('images/'+name,im_bw)
    # google vision start
    # client = vision.ImageAnnotatorClient()

    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'images/'+name)

    # with io.open(file_name, 'rb') as image_file:
    #     content = image_file.read()

    # image = types.Image(content=content)

    # response = client.text_detection(image=image) #api hit
    # labels = response.text_annotations
    # print('----------start----------')   
    # for label in labels:
    #     print("label : "+label.description) # print all the labels in image
    # print('----------end----------\n')
    # currentFrame += 1
    # cap.set(1,currentFrame)

cap.release()
cv2.destroyAllWindows()