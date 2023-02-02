from PyPDF2 import PdfWriter

merger = PdfWriter()

def merge_pdf(file_list, converted_filename):
    for pdf in file_list:
        merger.append(pdf)

    merger.write(f"file-database/merge-pdf/{converted_filename}")
    merger.close()