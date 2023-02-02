import tabula

def pdf_to_csv(filename, converted_filename):
    tabula.convert_into(
        f'file-database/pdf-to-csv/{filename}', 
        f'file-database/pdf-to-csv/{converted_filename}', 
        output_format='csv', 
        pages='all'
        )
