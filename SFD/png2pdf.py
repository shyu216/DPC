import fitz
import os
import glob

# bad resolution
from PIL import Image
def conv(path='.'):
    for name in glob.glob(os.path.join(path, '*.png')):

        image_1 = Image.open(name)
        im_1 = image_1.convert('RGB')
        im_1.save(name[:-4] + '.pdf')

def png2pdf(path='.'):
    for name in glob.glob(os.path.join(path, '*.png')):
        imgdoc = fitz.open(name)
        pdfbytes = imgdoc.convert_to_pdf()   
        imgpdf = fitz.open("pdf", pdfbytes)
        imgpdf.save(name[:-4] + '.pdf')

png2pdf()