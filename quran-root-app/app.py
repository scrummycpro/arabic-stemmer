import os
import re
import csv
from flask import Flask, request, render_template, redirect, url_for, send_file
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.isri import ISRIStemmer
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Ensure necessary NLTK resources are available
nltk.download('punkt')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder for storing uploaded files
app.secret_key = 'supersecretkey'  # Secret key for secure sessions

stemmer = ISRIStemmer()


def remove_diacritics(text):
    """Remove Arabic diacritics from text."""
    arabic_diacritics = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
    return arabic_diacritics.sub('', text)


def filter_arabic_text(file_path):
    """Filter Arabic characters and remove unwanted symbols."""
    arabic_pattern = re.compile(r'[\u0600-\u06FF]+')  # Match Arabic characters
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove diacritics
    text = remove_diacritics(text)

    # Extract Arabic words only
    arabic_words = arabic_pattern.findall(text)

    # Join the words into a single string
    cleaned_text = ' '.join(arabic_words)
    return cleaned_text


def process_arabic_text(cleaned_text):
    """Tokenize and stem Arabic text."""
    words = word_tokenize(cleaned_text)
    stemmed_words = [(word, stemmer.stem(word)) for word in words]
    return stemmed_words


def save_to_csv(stemmed_words, output_path):
    """Save stemmed words to a CSV file."""
    with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Original Word', 'Stemmed Word'])  # Header row
        writer.writerows(stemmed_words)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in request', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            # Save the uploaded file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Filter Arabic text and process it
            cleaned_text = filter_arabic_text(file_path)
            stemmed_words = process_arabic_text(cleaned_text)

            # Save cleaned text for export
            cleaned_text_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cleaned_text.txt')
            with open(cleaned_text_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

            # Save stemmed words to a CSV file
            csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'stemmed_results.csv')
            save_to_csv(stemmed_words, csv_path)

            return render_template(
                'result.html',
                cleaned_text=cleaned_text,
                stemmed_words=stemmed_words,
                cleaned_text_filename='cleaned_text.txt',
                csv_filename='stemmed_results.csv'
            )
    return render_template('index.html')


@app.route('/cleaned_text')
def cleaned_text_page():
    """Display the cleaned text on a separate page."""
    cleaned_text_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cleaned_text.txt')
    if os.path.exists(cleaned_text_path):
        with open(cleaned_text_path, 'r', encoding='utf-8') as file:
            cleaned_text = file.read()
        return render_template('cleaned_text.html', cleaned_text=cleaned_text)
    return "Cleaned text not found", 404


@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    """Download a file."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "File not found", 404


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Ensure the upload folder exists
    app.run(debug=True)