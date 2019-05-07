from PIL import Image
from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('frame1.jpg')))