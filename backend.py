from flask import Flask, request, jsonify, render_template
import joblib  # Assuming your ML model is serialized using joblib
import os
import supabase
from supabase import create_client, Client

app = Flask(__name__)

# Load your ML model (replace 'ml_model.pkl' with your actual model file)
model = joblib.load("ml_model.pkl")

# Supabase configuration
SUPABASE_URL = "https://haxbnnottbryxkrnekir.supabase.co/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhheGJubm90dGJyeXhrcm5la2lyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NDc4NDE4NSwiZXhwIjoyMDYwMzYwMTg1fQ.aJPOPAIeUMizyLBjDZ36gzLSZlSiCPBE9FKEWWDeOJ0"
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an `index.html` file

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    user_input = request.form['user_input']
    
    # Fetch file from Supabase
    file_name = request.form['file_name']  # Expecting a file name from the form
    try:
        response = supabase_client.storage.from_('bucket_name').download(file_name)
        with open(file_name, "wb") as f:
            f.write(response.content)
    except Exception as e:
        return jsonify({"error": str(e)})

    # Use the file and input for ML prediction
    # (You should replace this with your model's specific input preprocessing)
    input_data = preprocess(user_input, file_name)  # Define your preprocessing
    prediction = model.predict([input_data])  # Assuming the model expects a list

    return jsonify({"prediction": prediction.tolist()})

def preprocess(user_input, file_name):
    # Custom logic to prepare input for the ML model
    # Example: Combine user_input with data from the file
    with open(file_name, 'r') as file:
        file_data = file.read()
    return user_input + " " + file_data

if __name__ == '__main__':
    app.run(debug=True)
