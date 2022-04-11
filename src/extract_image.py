import os
from pdf2image import convert_from_path


def extract_images_from_pdf():
    for file in os.listdir('reports 2022'):
        pages = convert_from_path('reports 2022/' + file, 500)
        #pages[2].save('images/' + file.replace('.pdf', '.jpg'), 'JPEG')
        pages[2].save('images 2022/' + file + ".jpg", 'JPEG')
        print("Extracted " + file + " ...")
