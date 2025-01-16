Arabic Root Stemmer - Flask Application

This application processes Arabic text files to:
	1.	Filter Arabic text by removing non-Arabic characters and diacritics.
	2.	Extract stems of words using ISRIStemmer (an Arabic-specific stemmer).
	3.	Display cleaned text and processed results in a user-friendly interface.
	4.	Provide export options for cleaned text (as .txt) and processed results (as .csv).

Features
	•	Upload Arabic Text Files: Upload .txt files containing Arabic text for processing.
	•	Clean Arabic Text: Remove diacritics and non-Arabic characters.
	•	Stem Arabic Words: Extract stems using ISRIStemmer.
	•	View Results: Display cleaned text and stemmed results.
	•	Export Options: Download the cleaned text as a .txt file or the stemmed results as a .csv file.
	•	User-Friendly Interface: Responsive design with navigation links for easy access to different pages.

Installation and Setup

1. Clone the Repository

Clone the repository to your local machine:

git clone https://github.com/your-repo-name/ar-root-stemmer.git
cd ar-root-stemmer

2. Set Up a Virtual Environment

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install Dependencies

Install the required Python packages using pip:

pip install flask nltk

4. Download NLTK Resources

Ensure the necessary NLTK tokenizer model is downloaded:

import nltk
nltk.download('punkt')

5. Run the Application

Start the Flask application:

python app.py

Visit the application at http://127.0.0.1:5000/ in your web browser.

Usage

1. Upload a Text File
	1.	Navigate to the home page (http://127.0.0.1:5000/).
	2.	Upload a .txt file containing Arabic text.

2. View Processed Results
	•	After uploading, you’ll see:
	•	Cleaned Text: Arabic text with diacritics and non-Arabic characters removed.
	•	Stemmed Results: Original words and their extracted stems in a table.

3. Export Results
	•	Cleaned Text: Download as a .txt file.
	•	Stemmed Results: Download as a .csv file.

4. View Cleaned Text Separately
	•	Click on the View Cleaned Text button to navigate to a dedicated page displaying the cleaned text in a larger font.

Project Structure

ar-root-stemmer/
├── app.py                 # Main Flask application
├── uploads/               # Directory for uploaded files and exported results
├── templates/             # HTML templates for Flask
│   ├── base.html          # Base template with shared layout
│   ├── index.html         # Home page for file upload
│   ├── result.html        # Page to display processed results
│   ├── cleaned_text.html  # Page to display cleaned text
└── static/                # Static files (CSS, JS, images, etc.)

Detailed Explanation

Key Routes
	1.	Home (/):
	•	Displays the file upload form.
	•	Processes uploaded files and renders results.
	2.	Cleaned Text Page (/cleaned_text):
	•	Displays cleaned Arabic text on a separate page.
	3.	Download Files (/download/<filename>):
	•	Enables downloading of the cleaned text or stemmed results.

Text Processing
	•	Diacritic Removal:
	•	Removes Arabic diacritics using a regular expression.
	•	Filtering Arabic Characters:
	•	Retains only Arabic letters, removing numbers, punctuation, and other non-Arabic symbols.
	•	Word Stemming:
	•	Uses ISRIStemmer from NLTK to extract Arabic word roots.

Dependencies
	•	Python 3.6+
	•	Flask: For building the web application.
	•	NLTK: For tokenizing and stemming Arabic text.

Exported Files
	1.	Cleaned Text (cleaned_text.txt):
	•	Contains Arabic text with diacritics and non-Arabic characters removed.
	2.	Stemmed Results (stemmed_results.csv):
	•	A CSV file with two columns:
	•	Original Word
	•	Stemmed Word

Troubleshooting

Common Issues
	1.	Dependencies Missing:
	•	Ensure all dependencies are installed via pip install flask nltk.
	2.	NLTK Resources Not Found:
	•	Download the tokenizer model by running:

import nltk
nltk.download('punkt')


	3.	File Not Downloadable:
	•	Ensure the uploads folder exists and has write permissions:

mkdir uploads
chmod 755 uploads

Future Improvements
	•	Add More Export Formats: JSON and XML support for processed results.
	•	Enhance Arabic Stemming: Incorporate more advanced stemming algorithms for Arabic.
	•	Support for Other Languages: Extend processing capabilities to other languages.

License

This project is licensed under the MIT License.

Let me know if you need further clarifications or additions!