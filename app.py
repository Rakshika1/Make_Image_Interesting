from flask import Flask, render_template, request, send_file
import os
from processing.cartoon import cartoonify_image
from processing.warp import warp_image
from processing.grayscale import grayscale_image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'static/processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    effect = request.form['effect']  # Get selected effect from the form
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process the image based on selected effect
        processed_img_path = os.path.join(PROCESSED_FOLDER, f'{effect}_{file.filename}')
        if effect == 'cartoon':
            cartoonify_image(file_path, processed_img_path)
        elif effect == 'warp':
            warp_image(file_path, processed_img_path)
        elif effect == 'grayscale':
            grayscale_image(file_path, processed_img_path)

        return f'<h2>Effect Applied: {effect}</h2><img src="/{processed_img_path}" alt="Processed Image">'

if __name__ == '__main__':
    app.run(debug=True)
