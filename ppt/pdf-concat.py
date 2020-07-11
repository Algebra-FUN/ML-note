from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()
 
for i in range(18):
    merger.append(open(f'Lecture{i+1}.pdf', 'rb'))
 
with open('Lectures.pdf', 'wb') as fout:
    merger.write(fout)
