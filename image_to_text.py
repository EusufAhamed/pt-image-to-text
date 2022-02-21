# import pytesseract from the install library
import pytesseract as tess
# import Image from PIL(Pillow library)
from PIL import Image

# set the environment variable for tesseract_cmd which you already installed (Google Tesseract OCR)
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# open image with Pillow library
img = Image.open('Screenshot_38.png')
# convert image to text with pytesseract
text = tess.image_to_string(img)

# print the text
print(text)