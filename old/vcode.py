# #coding=utf-8
import pytesseract
from PIL import Image

image = Image.open(r'd:\app\22.png')
vcode = pytesseract.image_to_string(image)
print(vcode)

