import PyPDF2
from docx import Document

def pdf_to_docx(filename, converted_filename):
    with open(f'file-database/pdf-to-docx/{filename}', 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        
        # Create a new docx file
        doc = Document()
        
        # Iterate over each page in the PDF
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            content = page.extract_text()
            doc.add_paragraph(content)
            
        # Save the docx file
        doc.save(f"file-database/pdf-to-docx/{converted_filename}")