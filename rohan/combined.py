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
def finalSave(image,value):
    global iii
    iii = iii+1
    name = "image/"
    name += str(value)
    name += "/2v"

    name += str(iii)
    name+=".jpg"
    cv2.imwrite(name,image)
def insertIntoFolder(position,value,image):
    global iii
    if(position==0):
        im = image[0:28,28:41]
        finalSave(im,value)
    elif(position==1):
        im = image[0:28,41:54]
        finalSave(im,value)
    elif(position==2):
        im = image[0:28,254:68]
        finalSave(im,value)
    elif(position==3):
        im = image[0:28,68:82]
        finalSave(im,value)
    elif(position==4):
        im = image[0:28,82:96]
        finalSave(im,value)
    elif(position==5):
        im = image[0:28,96:110]
        finalSave(im,value)
    elif(position==6):
        im = image[0:28,110:123]
        finalSave(im,value)

    elif(position==7):
        im = image[0:28,166:183]
        finalSave(im,value)
    elif(position==8):
        im = image[0:28,183:196]
        finalSave(im,value)
    elif(position==9):
        im = image[0:28,196:211]
        finalSave(im,value)
    elif(position==10):
        im = image[0:28,211:225]
        finalSave(im,value)
    elif(position==11):
        im = image[0:28,223:238]
        finalSave(im,value)
    elif(position==12):
        im = image[0:28,238:252]
        finalSave(im,value)
    elif(position==13):
        im = image[0:28,252:268]
        finalSave(im,value)
    else:
        print("Else executed")
def finalfun(recievedImage):
    client = vision.ImageAnnotatorClient()
    content = recievedImage
    cv2.imwrite('temp.jpg',content)

    with io.open('temp.jpg', 'rb') as image_file:
        contentt = image_file.read()


    image = types.Image(content=contentt)


    response = client.text_detection(image=image) #api hit

    labels = response.text_annotations
    try:
        text = str(labels[0].description.replace(" ",""))
        text = text.replace(" ","")
        text = text.replace("\n","")
        print(text)
        a = {}
        if(len(text)>1):
            a[0]= str(text[1])
        if(len(text)>2):
            a[1]= str(text[2])
        if(len(text)>3):
            a[2]= str(text[3])
        if(len(text)>4):
            a[3]= str(text[4])
        if(len(text)>5):
            a[4]= str(text[5])
        if(len(text)>6):
            a[5]= str(text[6])
        if(len(text)>7):
            a[6]= str(text[7])

        if(len(text)>9):
            a[7]=   str(text[9])
        if(len(text)>10):
            a[8]=   str(text[10])
        if(len(text)>11):
            a[9]=   str(text[11])
        if(len(text)>12):
            a[10]=  str(text[12])
        if(len(text)>13):
            a[11]=  str(text[13])
        if(len(text)>14):
            a[12]=  str(text[14])
        # a[13]=  str(text[15])

        for val in a:
            # print(a[val])
            # if(int(a[val])>=0 or int(a[val])<=9):
            insertIntoFolder(val,a[val],content)    
        # print('----------start----------')
        # for label in labels:
        #     print("label : "+label.description) # print all the labels in image
    except:
        print ("This is an error message!")
    
i=0
cap = cv2.VideoCapture("videos/2.VOB")

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
    # cv2.imwrite(path_frame+name, im_bw)
    finalfun(im_bw)
    currentFrame+=1

cap.release()
cv2.destroyAllWindows()