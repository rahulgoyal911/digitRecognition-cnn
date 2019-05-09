import os
import io
import cv2
from google.cloud import vision
from google.cloud.vision import types
from PIL import ImageFilter, Image
#
# directory=''
# for filename in os.listdir(directory):
#     if filename.endswith(".asm") or filename.endswith(".py"):
#          # print(os.path.join(directory, filename))
#         continue
#     else:
#         continue



client = vision.ImageAnnotatorClient()

file_name = '/home/gaurav/Documents/textDetection/e.png'

content = cv2.imread(file_name)
res = cv2.resize(content, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imwrite('temp.jpg',res)

with io.open('temp.jpg', 'rb') as image_file:
    contentt = image_file.read()


image = types.Image(content=contentt)


response = client.text_detection(image=image) #api hit

labels = response.text_annotations
print('----------start----------')
for label in labels:
    print("label : "+label.description) # print all the labels in image