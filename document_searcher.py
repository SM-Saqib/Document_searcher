from curses.textpad import rectangle
from email.mime import image
from genericpath import exists
import os
from ocr_module import tesseract
from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont
# from fuzzywuzzy import fuzz


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

        output_df = tess_obj.get_ocr(images_path)
        return output_df

    def find_word(self, in_words,df):
        word_row = df.loc[df["text"].isin([in_words])]

        print(" row of the word from dataframe",word_row)

        for page_number in range(1,len(self.images_path)+1):

            page_word_rows = word_row.loc[word_row["page_num"].isin([page_number])]

            # page_number = word_row["page_num"]
            _image = self.images_path[0].split("-")[0] +"-"+ str(page_number) + ".jpg"
            self.word_boundingbox(_image,page_word_rows)
        return word_row



    def word_boundingbox(self , image_path, df_find):
        im = Image.open(image_path)
        draw = ImageDraw.Draw(im)


        for index , row in df_find.iterrows():
            vec_bb = [row['left'], row['top'], row['width']+row['left'], row['height']+row['top'] ]
            print(vec_bb)

            # fnt = ImageFont.load_default()

            draw.rectangle(vec_bb,fill =None, outline ="red",width=4)
        im.show()







    # def get_ocr_pdf(pdf_path):
def main():
    doc_search_obj = document_searcher()
    df_pdf = doc_search_obj.load_ocr("/media/saqib/VolumeD/mywork/Django/Document_searcher/data/inputpdfs/HospitalMedicalReport.pdf")
    doc_search_obj.find_word("Hospital",df_pdf)


if __name__ == "__main__":
    main()
