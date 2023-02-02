from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(filename, converted_filename):
    reader = PdfReader(f'file-database/compress-pdf/{filename}')
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    writer.add_metadata(reader.metadata)
    writer.remove_images()

    with open(f'file-database/compress-pdf/{converted_filename}', "wb") as f:
        writer.write(f)