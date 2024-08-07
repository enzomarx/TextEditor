from flask import Flask, request, render_template, redirect, url_for
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            text = pytesseract.image_to_string(Image.open(file_path))
            return render_template('index.html', text=text)
    return render_template('index.html', text='')

if __name__ == '__main__':
    app.run(debug=True)