from ocr_module import tesseract
from NER import spacy_ner
import os
import pandas

def test_1():
  for root, dirs, files in os.walk("/content/drive/MyDrive/Document_searcher/input_images"):
    for file in files:

      image_path = os.path.join(root,file)
      text_page= tesseract.get_ocr_single_image(image_path)
      with open("/content/select_images_ocr/"+file+".txt","w") as file:
        file.write(text_page)

      ner = spacy_ner()
      ner._to_spacy_token(text_page)

    




test_1()
