import PyPDF2


import PyPDF2

def merge_pdfs(file_paths, output_path):
    merger = PyPDF2.PdfMerger()

    for path in file_paths:
        merger.append(path)

    merger.write(output_path)
    merger.close()

# Example usage
pdf_files = ['C:/Users/yash/Documents/PDF/1.pdf', 'C:/Users/yash/Documents/PDF/2.pdf', 'C:/Users/yash/Documents/PDF/3.pdf','C:/Users/yash/Documents/PDF/4.pdf','C:/Users/yash/Documents/PDF/5.pdf']
output_file = 'C:/Users/yash/Documents/PDF/result/merged.pdf'

merge_pdfs(pdf_files, output_file)

from PyPDF2 import PdfMerger
print(dir(PyPDF2))
def merge_pdfs(file_paths):
    merger = PyPDF2.PdfWriter()

    for path in file_paths:
        merger.write(path)

    merger.write(path)
    merger.close()



# Example usage
pdf_files = ['C:/Users/yash/Documents/PDF/A.pdf', 'C:/Users/yash/Documents/PDF/B.pdf', 'C:/Users/yash/Documents/PDF/c.pdf','C:/Users/yash/Documents/PDF/D.pdf','C:/Users/yash/Documents/PDF/E.pdf']



merge_pdfs(pdf_files)




