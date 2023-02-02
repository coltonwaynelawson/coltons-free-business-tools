from flask import Flask, render_template, request, send_from_directory, url_for, session
from werkzeug.utils import secure_filename
import random
import os

from functions.ocr import extract_text
from functions.pdf_to_csv import pdf_to_csv
from functions.pdf_to_xlsx import pdf_to_xlsx
from functions.pdf_to_docx import pdf_to_docx
from functions.compress_pdf import compress_pdf
from functions.pdf_to_text import pdf_to_text
from functions.merge_pdf import merge_pdf

from database import app, db, Feedback

@app.route('/')
def index():
    # track the number of times a user has submitted a form and if none then set the click count to 0.
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('home.html')


@app.route('/ocr', methods=['GET', 'POST'])
def route_image_to_text():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists('file-database/ocr'):
                os.makedirs('file-database/ocr')
            rand = generate_random_string()
            new_filename = f'{rand}_{filename}'
            file.save(f'file-database/ocr/{new_filename}')
            text = extract_text(file)
            return render_template('ocr.html', text=text)
    else:
        # Render the template without passing any data
        return render_template('ocr.html')


@app.route('/pdf-to-csv', methods=['GET', 'POST'])
def route_pdf_to_csv():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists('file-database/pdf-to-csv'):
                os.makedirs('file-database/pdf-to-csv')
            rand = generate_random_string()
            new_filename = f'{rand}_{filename}'
            file.save(f'file-database/pdf-to-csv/{new_filename}')
            converted_filename = f"{rand}_converted_{filename[:-4]}.csv"
            pdf_to_csv(new_filename, converted_filename)
            return render_template('pdf-to-csv.html', filename=converted_filename)
    else:
        return render_template('pdf-to-csv.html')


@app.route('/database_download/pdf_to_csv/<filename>')
def database_download_pdf_to_csv(filename):
    return send_from_directory('file-database/pdf-to-csv', filename)


@app.route('/pdf-to-xlsx', methods=['GET', 'POST'])
def route_pdf_to_xlsx():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists('file-database/pdf-to-xlsx'):
                os.makedirs('file-database/pdf-to-xlsx')
            rand = generate_random_string()
            new_filename = f'{rand}_{filename}'
            file.save(f'file-database/pdf-to-xlsx/{new_filename}')
            converted_filename = f"{rand}_converted_{filename[:-4]}.xlsx"
            pdf_to_xlsx(new_filename, converted_filename)
            return render_template('pdf-to-xlsx.html', filename=converted_filename)
    else:
        return render_template('pdf-to-xlsx.html')


@app.route('/database_download/pdf_to_xlsx/<filename>')
def database_download_pdf_to_xlsx(filename):
    return send_from_directory('file-database/pdf-to-xlsx', filename)


@app.route('/pdf-to-docx', methods=['GET', 'POST'])
def route_pdf_to_docx():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists('file-database/pdf-to-docx'):
                os.makedirs('file-database/pdf-to-docx')
            rand = generate_random_string()
            new_filename = f'{rand}_{filename}'
            file.save(f'file-database/pdf-to-docx/{new_filename}')
            converted_filename = f"{rand}_converted_{filename[:-4]}.docx"
            pdf_to_docx(new_filename, converted_filename)
            return render_template('pdf-to-docx.html', filename=converted_filename)
    else:
        return render_template('pdf-to-docx.html')


@app.route('/database_download/pdf_to_docx/<filename>')
def database_download_pdf_to_docx(filename):
    return send_from_directory('file-database/pdf-to-docx', filename)


@app.route('/compress-pdf', methods=['GET', 'POST'])
def route_compress_pdf():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists('file-database/compress-pdf'):
                os.makedirs('file-database/compress-pdf')
            rand = generate_random_string()
            new_filename = f'{rand}_{filename}'
            file.save(f'file-database/compress-pdf/{new_filename}')
            converted_filename = f"{rand}_converted_{filename[:-4]}.pdf"
            compress_pdf(new_filename, converted_filename)
            return render_template('compress-pdf.html', filename=converted_filename)
    else:
        return render_template('compress-pdf.html')


@app.route('/database_download/compress_pdf/<filename>')
def database_download_compress_pdf(filename):
    return send_from_directory('file-database/compress-pdf', filename)


@app.route('/pdf-to-text', methods=['GET', 'POST'])
def route_pdf_to_text():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists('file-database/pdf-to-text'):
                os.makedirs('file-database/pdf-to-text')
            rand = generate_random_string()
            new_filename = f'{rand}_{filename}'
            file.save(f'file-database/pdf-to-text/{new_filename}')
            text = pdf_to_text(file)
            return render_template('pdf-to-text.html', text=text)
    else:
        return render_template('pdf-to-text.html')


@app.route('/merge-pdf', methods=['GET', 'POST'])
def route_merge_pdf():
    if 'counter' not in session:
        session['counter'] = 0
    file_list = None
    if request.method == 'POST':
        session['counter'] += 1
        file_list = request.files.getlist('file')
        rand = generate_random_string()
        if file_list:
            for file in file_list:
                filename = secure_filename(file.filename)
                if not os.path.exists('file-database/merge-pdf'):
                    os.makedirs('file-database/merge-pdf')
                new_filename = f'{rand}_{filename}'
                file.save(f'file-database/merge-pdf/{new_filename}')
            converted_filename = f"{rand}_merged_file.pdf"
            merge_pdf(file_list, converted_filename)
            return render_template('merge-pdf.html', filename=converted_filename)
    else:
        return render_template('merge-pdf.html')


@app.route('/database_download/merge_pdf/<filename>')
def database_download_merge_pdf(filename):
    return send_from_directory('file-database/merge-pdf', filename)


# submit the feedback form
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    feedback_submit = Feedback(name=request.form['name'], feedback_description = request.form['feedback'])
    db.session.add(feedback_submit)
    db.session.commit()
    return 'Thanks for your feedback!'


@app.route('/terms-of-use')
def tos():
    # track the number of times a user has submitted a form and if none then set the click count to 0.
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('terms-of-use.html')


def generate_random_string():
    return "".join(chr(random.randint(48, 57)) for i in range(4))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)