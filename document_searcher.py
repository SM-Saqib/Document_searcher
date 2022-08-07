from genericpath import exists
import os
from ocr_module import tesseract
from pdf2image import convert_from_path


class document_searcher():
    def __init__(self):
        self.save_dir = "/media/saqib/VolumeD/mywork/Django/Document_searcher/data/pdf_images/"
        self.images_path = []

    def pdf_to_images(self,pdf_path):

        output_path = os.path.join(self.save_dir , pdf_path.split("/")[-1].split(".pdf")[0])
        
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        # save the images    
        self.images_path=convert_from_path(pdf_path,
        output_folder = output_path,
        output_file = pdf_path.split("/")[-1].split(".pdf")[0],
        fmt = "jpg",
        paths_only = True,
        )
        return self.images_path

    def load_ocr(self,pdf_path):
        tess_obj = tesseract()
        images_path = self.pdf_to_images(pdf_path)

        output_dict = tess_obj.get_ocr(images_path)
        print(tess_obj.pdf_ocr_dict)
        # print("tess dict" , output_dict)



    # def get_ocr_pdf(pdf_path):
def main():
    doc_search_obj = document_searcher()
    doc_search_obj.load_ocr("/media/saqib/VolumeD/Veeve/Dcube_stuff/Data/J2 Global-20220225T043505Z-001/esi.pdf")


if __name__ == "__main__":
    main()
