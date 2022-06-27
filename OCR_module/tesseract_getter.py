from PIL import Image
import pytesseract
import os

class tesseract():
  def __init__(self):
    pass

  def get_ocr_single_image(image_path):
    ## loading the image using PIL
    image = Image.open(image_path)


    image = image.convert('L')

    text = pytesseract.image_to_string(image)
    return text

  

