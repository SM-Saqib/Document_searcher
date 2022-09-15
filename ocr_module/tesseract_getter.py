from email.mime import image
from PIL import Image
import pytesseract
from pytesseract import Output

import os
import pandas as pd

class tesseract():
  def __init__(self):
    self.pdf_ocr_dict = {}
    self.full_ocr_df = pd.DataFrame()

  def get_ocr_single_image(self,image_path, get_bounding_box = False):
    ## loading the image using PIL
    image = Image.open(image_path)


    image = image.convert('L')
    if get_bounding_box:
      text = pytesseract.image_to_data(image, output_type = Output.DICT)
      # text = pytesseract.image_to_data(image)
      dataframe = pd.DataFrame.from_dict(text)
      return dataframe


      

    else:
      text = pytesseract.image_to_string(image)
      
    return text

  def get_ocr(self, image_path_list):
    images = [img.split("/")[-1] for img in image_path_list]# if ".png" in img]
    # print("images : ",images)
    list_dfs = []
    for full_path,image_name in zip(image_path_list,images):
      page_number = int(image_name.split("-")[-1].split(".jpg")[0])
      print(page_number)

      ocr_df = self.get_ocr_single_image(full_path,True)
      # ocr_df.loc[ocr_df['page_num'],'page_num'] = page_number
      ocr_df["page_num"] = page_number


      list_dfs.append(ocr_df)

      # break
    self.full_ocr_df = pd.concat(list_dfs , ignore_index = True)

    self.full_ocr_df.to_csv(os.path.join("/media/saqib/VolumeD/mywork/Django/Document_searcher/data/csv_output",full_path.split("/")[-2]) + ".csv")
    return self.full_ocr_df




  

