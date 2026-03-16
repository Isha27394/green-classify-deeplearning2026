import numpy as np
import os
from flask import Flask, request, render_template
try:
    from keras.models import load_model
    from keras.utils import load_img, img_to_array
    KERAS_AVAILABLE = True
except ImportError:
    KERAS_AVAILABLE = False

# Get the flask directory path
flask_dir = os.path.join(os.path.dirname(__file__), '..', 'flask')

app = Flask(__name__, 
            template_folder=os.path.join(flask_dir, 'templates'),
            static_folder=os.path.join(flask_dir, 'static'))

# Loading the model
model = None
model_path = os.path.join(flask_dir, "vegetable_classification.h5")
if KERAS_AVAILABLE and os.path.exists(model_path):
    model = load_model(model_path, compile=False)
    print("Model loaded successfully!")
else:
    print(f"Warning: Model file not found or Keras not available.")
    print("Please train the model and run locally.")

# Default home page or route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction.html')
def prediction():
    return render_template('prediction.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/logout.html')
def logout():
    return render_template('logout.html')

@app.route('/result', methods=["GET", "POST"])
def res():
    if request.method == "POST":
        if model is None or not KERAS_AVAILABLE:
            return render_template('prediction.html', pred="Model not loaded or Keras not available! Please run locally for full features.")
        
        f = request.files['image']
        uploads_dir = os.path.join(flask_dir, 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)
        filepath = os.path.join(uploads_dir, f.filename)
        f.save(filepath)
        
        # Reading Image - resize to (224, 224) to match model input
        img = load_img(filepath, target_size=(224, 224))
        img_arr = img_to_array(img)
        img_arr = img_arr / 255.0  # Normalize if model was trained with normalization
        img_input = np.expand_dims(img_arr, axis=0)
        # Predicting the higher probability index
        pred = np.argmax(model.predict(img_input))
        # Class mapping
        op = {
            0: 'Bean', 
            1: 'Bitter_Gourd', 
            2: 'Bottle_Gourd', 
            3: 'Brinjal', 
            4: 'Broccoli', 
            5: 'Cabbage', 
            6: 'Capsicum', 
            7: 'Carrot', 
            8: 'Cauliflower', 
            9: 'Cucumber', 
            10: 'Papaya', 
            11: 'Potato', 
            12: 'Pumpkin', 
            13: 'Radish', 
            14: 'Tomato'
        }
        
        result = op[pred]
        return render_template('prediction.html', pred=result)

""" Running our application """
if __name__ == "__main__":
    app.run(debug=True)
