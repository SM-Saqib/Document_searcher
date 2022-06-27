from ocr_module import tesseract

def test_1():
  image_path = "/content/drive/MyDrive/Document_searcher/recv-fax-56890405-2.png"
  text_page= tesseract.get_ocr_single_image(image_path)
  with open(image_path+".txt","w") as file:
    file.write(text_page)
    


test_1()
