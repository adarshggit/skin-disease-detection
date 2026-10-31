
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load the trained model
model = load_model('final_model.keras')

# Define the list of classes corresponding to the diseases
classes = [
    'Cold sores',
    'Ichthyosis',
    'Ringworm',
    'Vitiligo',
    'Acne',
    'Eczema',
    'Psoriasis'
]

# Map classes to HTML files
class_to_html = {
    'Cold sores': 'cold_sores.html',
    'Ichthyosis': 'ichthyosis.html',
    'Ringworm': 'ringworm.html',
    'Vitiligo': 'vitiligo.html',
    'Acne': 'acne.html',
    'Eczema': 'eczema.html',
    'Psoriasis': 'psoriasis.html'
}


# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# Check whether the uploaded file is valid
def allowed_file(filename):
    return (
        '.' in filename
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        # Check whether file exists in request
        if 'file' not in request.files:
            return render_template(
                'index.html',
                error="No file part in the request."
            )

        file = request.files['file']

        # Check whether a file was selected
        if file.filename == '':
            return render_template(
                'index.html',
                error="Please select an image."
            )

        # Check file extension
        if not allowed_file(file.filename):
            return render_template(
                'index.html',
                error="Please upload a valid image file."
            )

        try:

            # Generate a unique filename
            filename = secure_filename(file.filename)

            unique_filename = f"{uuid.uuid4()}_{filename}"

            # Save uploaded image
            os.makedirs("static", exist_ok=True)

            img_path = os.path.join("static", unique_filename)

            file.save(img_path)

            # Preprocess image
            img = load_img(img_path)

            img = img.resize((128, 128))

            img_array = img_to_array(img) / 255.0

            img_array = np.expand_dims(img_array, axis=0)

            # Make prediction
            prediction = model.predict(img_array)

            predicted_class = classes[np.argmax(prediction)]

            confidence = np.max(prediction)

            # Get corresponding treatment HTML
            prescription_html = class_to_html.get(
                predicted_class,
                None
            )

            # Render prediction result
            return render_template(
                'index.html',
                predicted_class=predicted_class,
                confidence=f"{confidence:.2f}",
                prescription_html=prescription_html,
                img_path=img_path
            )

        except Exception as e:

            # Display processing errors in popup
            return render_template(
                'index.html',
                error=f"Image processing error: {str(e)}"
            )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
