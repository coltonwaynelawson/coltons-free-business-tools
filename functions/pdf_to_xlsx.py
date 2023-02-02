import tabula

def pdf_to_xlsx(filename, converted_filename):
    df = tabula.read_pdf(f'file-database/pdf-to-xlsx/{filename}', pages = 'all')[0]
    df.to_excel(f'file-database/pdf-to-xlsx/{converted_filename}', index=None)