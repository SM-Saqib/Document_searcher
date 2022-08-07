from PIL import Image
import pytesseract
from pytesseract import Output

import os

class tesseract():
  def __init__(self):
    self.pdf_ocr_dict = {}

  def get_ocr_single_image(self,image_path, get_bounding_box = False):
    ## loading the image using PIL
    image = Image.open(image_path)


    image = image.convert('L')
    if get_bounding_box:
      text = pytesseract.image_to_data(image, output_type = Output.DICT)
      

    else:
      text = pytesseract.image_to_string(image)
      
    return text

  def get_ocr(self, image_path_list):
    images = [img.split("/")[-1] for img in image_path_list]# if ".png" in img]
    for full_path,image_name in zip(image_path_list,images):
      ocr_dict = self.get_ocr_single_image(full_path,True)
      
      self.pdf_ocr_dict[image_name] = ocr_dict
    return self.pdf_ocr_dict




  

